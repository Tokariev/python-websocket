import socket


SERVER_ADDRESS = ('127.0.0.1', 5001)

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

server_socket.bind(SERVER_ADDRESS)
server_socket.listen(5)
print('Server is listening...')

while True:
    (client_socket, address) = server_socket.accept()
    msg = client_socket.recv(1024)
    print(msg.decode('utf-8'))
    client_socket.send(bytes('Hello Client', 'utf-8'))