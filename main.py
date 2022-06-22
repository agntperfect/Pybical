from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

HOST = "127.0.0.1"
PORT = 80

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Hello World!</title></head><body><h1>Hello World!</h1></body></html>", "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type",  "application/JSON")
        self.end_headers()

        x = datetime.datetime.now()
        self.wfile.write(bytes("{'date': '"+ str(x) +"'}\n", "utf-8"))

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server close...")