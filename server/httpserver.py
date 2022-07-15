from http.server import BaseHTTPRequestHandler, HTTPServer
import os
HOST = "127.0.0.1"
PORT = 80

class NeuralHTTP(BaseHTTPRequestHandler):
   def do_GET(self):
        if self.path == '/':
            self.path = '/static/www/index.html' or '/static/www/index.htm'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)