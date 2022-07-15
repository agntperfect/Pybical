import ssl
import time
from http.server import HTTPServer
from server.httpserver import NeuralHTTP

HOST_NAME = 'localhost'
PORT = 80

if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME,PORT),NeuralHTTP)
    print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME,PORT))

    # SSL configuration
    """ 
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
    """
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('\n',time.asctime(),'Stop Server - %s:%s' %(HOST_NAME,PORT))
        pass