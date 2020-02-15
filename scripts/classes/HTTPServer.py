"""
    (c) 2020. Matej Arlović, Franjo Josip Jukić
"""
import socket
import threading
from httplib import HTTPResponse
from StringIO import StringIO
from json_parser import JSONParser
import time
from datetime import datetime, timedelta

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
		HTTP server class that handles all HTTP data given from the client.
	"""

	def __init__(self, port=8888, client=None):
		"""
			HTTP Server constructor

			:params port: Server port (default is 8888)
			:params client: Client class instance
		"""
		self.client = client
		self.host = ''
		self.port = port
		

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
		headers += 'Date: {now}\n'.format(now=time_now)
		headers += 'Server: MusicResearch-Server\n'
		headers += 'Connection: close\n\n'
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
		return whole_data.split('\r\n\r\n')[1]
		

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
				print("[BENCHMARK]: average (" + str((bench_end_time-bench_start_time).total_seconds()) + ")")
				break

			parsed_request = self.parse_data(request_data)
			json_parser = JSONParser(parsed_request.decode('utf-8'))
			data = json_parser.json_to_list(json_parser.data)
			response = None

			if json_parser.type == "2810":
				response = self.client.make_prediction(json_parser.predicttype, data)
			elif json_parser.type == "2015":
				response = self.client.save_prediction_data(json_parser.predicttype, data, json_parser.diagnosis)
		
			print(response)
			self.write_response(client_sock, response)

			bench_end_time = datetime.now()
			print("[BENCHMARK]: average (" + str((bench_end_time-bench_start_time).total_seconds()) + ")")
			break