import threading
from settings import *
from main import Socket


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.bind(IP_PORT)
        self.listen(5)
        print('Server is listening')
        self.users = []

    def send_data(self, data, user, address):
        for use in self.users:
            if user != use:
                use.send(f'{address} -> {data.decode()}'.encode())

    def listen_socket(self, user, address):
        print('listening')
        while True:
            data = user.recv(MAX)
            print('user send', data.decode('utf-8'))
            self.send_data(data, user, address)

    def start(self):
        while True:
            user_socket, address = self.accept()
            print(f'user: <{address[0]}> connected!!')
            self.users.append(user_socket)
            listen_accept_user = threading.Thread(target=self.listen_socket, args=(user_socket, address))
            listen_accept_user.start()


if __name__ == '__main__':
    al = Server()
    al.start()
