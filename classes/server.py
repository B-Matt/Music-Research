"""
    (c) 2020. Matej Arlović, Franjo Josip Jukić
"""
from . import blobstorage as bs
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class ServerHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        uuid = str(self.path).split('=')
        
        try:            
            logging.info("GET request,\nPath: %s\n", str(uuid[1]))
            self._set_response()
            self.wfile.write("Does {} exists? {}".format(str(uuid[1]), self.handle_storage(uuid[1])).encode('utf-8'))
        except Exception:
            pass

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def handle_storage(self, uuid):
        storage = bs.BlobStorage()
        return storage.get_blob_folder(uuid)

class HttpServer(object):
    def run(self, server_class=HTTPServer, handler_class=ServerHandler, port=8080):
        logging.basicConfig(level=logging.INFO)
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        logging.info('[HTTP SERVER]: Starting...')

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
        logging.info('[HTTP SERVER]: Stopping...')