import os, json, socket, threading, time, shutil
import audio_ffmpeg as ffmpeg
import features as af
from httplib import HTTPResponse
from StringIO import StringIO
from datetime import datetime, timedelta
import BlobStorage as bs

class ParseResponse():
	"""
		Helper class made for parsing HTTP response string
	"""
	def __init__(self, response_str):
		self._file = StringIO(response_str)
		
	def makefile(self, *args, **kwargs):
		return self._file

class HTTPServer(object):
	"""
		HTTP server class
	"""
	
	storage_uri = "https://mrsongs.blob.core.windows.net/assets/"

	def __init__(self, port=8888):
		"""
			HTTP Server constructor

			:params port: Server port (default is 8888)
			:params client: Client class instance
		"""
		self.host = '0.0.0.0'
		self.port = port
		self.blob_storage = bs.BlobStorage()
		

	def start(self):
		"""
			Starts HTTP server if there is no errors.
		"""
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		try:
			print("[INFO]: Starting HTTP server (" + str(self.host) + ":" + str(self.port) +")!")
			self.socket.bind((self.host, self.port))
			self.socket.listen(5)
			self.listen_socket()
			self.isServerOnline = True
		except Exception as e:
			print("[ERROR]: Stopping HTTP server!")
			print(e)
			self.shutdown()


	def shutdown(self):
		"""
			Shutsdown HTTP server.
		"""
		try:
			print("[INFO]: Stopping HTTP server via function shutdown()!")
			self.socket.shutdown(socket.SHUT_RDWR)
			self.socket.close()
			self.isServerOnline = False
		except Exception as e:
			pass

	def _set_headers(self, response_code):
		"""
			Create HTTP header data based on response_code.

			:params response_code: Response code that is returning in return HTTP response
		"""
		headers = ''
		if response_code == 200:
			headers += 'HTTP/1.1 200 OK\n'
		elif response_code == 404:
			headers += 'HTTP/1.1 404 Not Found\n'

		time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		headers += 'Content-Type: application/json; charset=utf-8\n'
		headers += 'Content-Encoding: gzip\n'
		headers += 'Date: {now}\n'.format(now=time_now)
		return headers

	def listen_socket(self):
		"""
			Listens server socket for new clients. If there is new client new server thread is created,
		"""
		while True:
			try:
				(client, address) = self.socket.accept()
				client.settimeout(60)
				threading.Thread(target=self.handle_client, args=(client, address)).start()
			except KeyboardInterrupt:
				if client:
					client.close()
				break

	def parse_data(self, request_data):
		"""
			Parses HTTP request data
		"""
		source = ParseResponse(request_data)
		response = HTTPResponse(source)
		response.begin()
		whole_data = response.read(len(request_data))
		return whole_data
		

	def write_response(self, client, data):
		"""
			Sends back response to a client.

			:params client: Socket of a client
			:params data: Data what server sends back to client
		"""
		response = self._set_headers(200).encode('utf-8')
		response += data
		client.send(response.encode('utf-8'))
		client.close()

	def extract_features(self, song):
		"""
		Extracts features from given Blob hosted on Azure BlobStorage.
		
		Returns
		-------
		features : List
				List of features extracted from the Blob.		
		"""
		song_directory = os.path.normpath(os.getcwd() + "/songs/")
		segments_len = 30
		
		song_path, blob_uri = self.blob_storage.format_blob_path(song) 
		output_path = os.path.normpath(song_directory + "/" + os.path.dirname(song))
		
		try:
			os.makedirs(output_path)
		except Exception:
			pass
			
		ffmpeg_song = ffmpeg.AudioFFmpeg()

		## Generate Segments
		length = ffmpeg_song.get_audio_length(song_path)
		if length > 31:
			ffmpeg_song.generate_audio_segments(song_path, output_path, segments_len)        

		## Get Audio File Features
		segments = round(round(length / segments_len) / 2)
		song_features = af.AudioFeatures(output_path)

		## Show Features
		features = song_features.format_song_features(length, (segments, segments + 1))
		
		## Remove blobs from the storage (Blob & VM Storage)
		shutil.rmtree(output_path, ignore_errors = False)
		self.blob_storage.remove_blob(song)
		return features

	def handle_client(self, client_sock, address):
		"""
			Thread that handles a clients connected to HTTP server.

			:params client_sock: Socket of a client
			:params address: Clients address
		"""
		packet_size = 1024
		while True or self.isServerOnline:
			bench_start_time = datetime.now()
			print("[INFO]: HTTP request is received at " + bench_start_time.strftime("%H:%M:%S %d-%m-%Y"))
			request_data = client_sock.recv(packet_size).encode('latin-1').decode('utf-8')
			
			if not request_data:
				bench_end_time = datetime.now()
				print("[INFO]: Request is empty! (avg. time " + str((bench_end_time-bench_start_time).total_seconds()) + ")")
				break

			parsed_request = self.parse_data(request_data)
			request = json.loads(parsed_request.decode('utf-8'))
			
			features = self.extract_features(request['blob_path'])			
			self.write_response(client_sock, json.dumps(features))
			bench_end_time = datetime.now()
			
			print("[INFO]: Request is done! (avg. time " + str((bench_end_time-bench_start_time).total_seconds()) + ")")
			break
