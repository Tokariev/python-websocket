import socket
import time


SERVER_ADDRESS = ('127.0.0.1', 5002)

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

print('I am Server\n')
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(5)

while True:
    (client_socket, address) = server_socket.accept()
    msg = client_socket.recv(1024)
    print(msg.decode('utf-8'))
    client_socket.send(bytes('Hello Client\n', 'utf-8'))

    for i in range(10):
        client_socket.send(bytes(str(i), 'utf-8'))
        time.sleep(1)