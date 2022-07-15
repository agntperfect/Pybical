from os import execv
import socket
import threading
import sys

try: 
    HOST_IP = input("Enter Host's IP: ")
    print(f"{type(HOST_IP)}")
    if HOST_IP == "":
        print("Please Enter Host's IP.")
except:
    print("Something else went wrong. Please try again")


try:
    HOST_PORT = int(input("Enter Host's PORT: "))
    print(f"{type(HOST_PORT)}")
    if HOST_PORT == "":
        print("Please Enter Host's port.")
except ValueError:
    print("Please enter in number")
except KeyboardInterrupt: 
    print("exit")
    sys.exit(1)

nickname = input("Choose a nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST_IP, HOST_PORT))
except NameError:
    print("Host port is empty")
    sys.exit(1)
except KeyboardInterrupt:
    print("exit")
    sys.exit(1)
except ConnectionRefusedError:
    print("Your host refuse to connect.")
    sys.exit(1)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()