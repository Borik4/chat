import socket
class Socket(socket.socket):
    def __init__(self):
        super(Socket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

    def send_data(self, data, user, address):
        raise NotImplementedError()
    def listen_socket(self, user, address):
        raise NotImplementedError()
