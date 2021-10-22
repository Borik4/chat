import socket
import threading
from settings import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(IP_PORT)
server.listen(5)
users = []

def send_all(data):
    for user in users:
        print(user)
        user.send(data)


def listen_user(user):
    print('listening')
    while True:
        data = user.recv(2048)
        print('user send', data)
        send_all(data)

def start():
    while True:
        user_socket, address = server.accept()
        print(f'user: <{address[0]}> connected!!')
        users.append(user_socket)
        listen_accept_user = threading.Thread(target=listen_user, args=(user_socket,))
        listen_accept_user.start()


if __name__ == '__main__':
    start()


