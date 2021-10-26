import socket
from threading import Thread
from settings import *
from rich import print as pr

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(IP_PORT)


def listen_server():
    while True:
        data = client.recv(MAX)
        pr(data.decode(ENCODING))


def send_server():
    pr('[red]input name[/red] ', end='')
    client.send(input().encode())
    # user_name()
    lis_tread = Thread(target=listen_server)
    lis_tread.start()
    while True:
        client.send(input().encode(ENCODING))


def user_name():
    while True:
        pr('[red]input name[/red] ', end='')
        client.send(input().encode())
        if client.recv(MAX).decode(ENCODING) != '0':
            break
        print('username is not available')


if __name__ == '__main__':
    send_server()
