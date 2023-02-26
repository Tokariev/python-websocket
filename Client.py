import socket


SERVER_ADDRESS = ('127.0.0.1', 5001)

client_socket = socket.socket(socket.AF_INET,     #Internet Protocol
                              socket.SOCK_STREAM) #TCP Protocol


client_socket.connect(SERVER_ADDRESS)
client_socket.send(bytes('Hello Server', 'utf-8'))

while True:
    msg = client_socket.recv(1024)
    print(msg.decode('utf-8'))

