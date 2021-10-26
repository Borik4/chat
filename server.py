import threading
from settings import *
from main import Socket


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.bind(IP_PORT)
        self.listen(5)
        print('Server is listening')
        self.users_names = {}

    def send_data(self, data, user, address):
        for use in self.users_names:
            if user != use:
                l = '[red]' + self.users_names[user] + '[/red]' + '                           ' + data.decode()
                print(l)
                use.send(l.encode())

    def listen_socket(self, user, address):
        print('listening')
        name = user.recv(MAX).decode(ENCODING)
        print(name)
        self.users_names[user] = name
        while True:
            data = user.recv(MAX).decode(ENCODING)
            print(data)
            if data == '':
                self.send_data(f'{self.users_names[user]} disconnect'.encode(ENCODING), user, address)
                exit()
            print('user send', data)
            self.send_data(data.encode(ENCODING), user, address)

    def start(self):
        while True:
            user_socket, address = self.accept()
            print(f'user: <{address[0]}> connected!!')
            listen_accept_user = threading.Thread(target=self.listen_socket, args=(user_socket, address))
            listen_accept_user.start()


if __name__ == '__main__':
    al = Server()
    al.start()
