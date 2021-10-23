import socket
import threading
from settings import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(IP_PORT)
server.listen(5)
users = []


def send_all(data, user, address):
    for use in users:
        if user != use:
            use.send(f'{address} -> {data.decode()}'.encode())


def listen_user(user, address):
    print('listening')
    while True:
        data = user.recv(MAX)
        print('user send', data.decode('utf-8'))
        send_all(data, user, address)


def start():
    while True:
        user_socket, address = server.accept()
        print(f'user: <{address[0]}> connected!!')
        users.append(user_socket)
        listen_accept_user = threading.Thread(target=listen_user, args=(user_socket, address))
        listen_accept_user.start()


if __name__ == '__main__':
    start()
