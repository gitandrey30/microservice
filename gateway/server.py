import http
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

PORT = 3000

class ServerHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(ServerHandler, self).end_headers()

    def do_GET(self):
        global data
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        path = self.path
        if path == '/currency':
            data = requests.get('http://127.0.0.1:8080/')
        self.wfile.write(bytes(data))
httpd = http.server.HTTPServer(('localhost', PORT), ServerHandler)
print('server work on', PORT, 'port')
httpd.serve_forever()




#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         if self.path == '/weather':
#             data = requests.get('http://127.0.0.1:8000/').json()
#         elif self.path == '/currency':
#             data = requests.get('http://127.0.0.1:5000/').json()
#         self.wfile.write(json.dumps(data).encode())
#
#     def do_POST(self):
#         self.send_response(200)
#         self.send_header('content_type', 'text/html')
#         self.end_headers()
#         if self.path == '/login':
#             content_len = int(self.headers.get('Content-type'))
#             post_body =self.rfile.read(content_len)
#             print(post_body.decode())
#             data = post_body.decode()
#             requests.post('http://127.0.0.1:8080/login', data=data)
#


