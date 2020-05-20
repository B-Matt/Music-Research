from http_server import HTTPServer

server = HTTPServer(8888)
server.start()
server.shutdown()
