'''
This code was created from a toutorial which is:
https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-receiving-information/
The code has been adapted to meet the needs for this project.
'''

# creating a network to play pong on
import socket


class network:
    def __init__(self):
        # connects the client (PongMain) to a socket.
        self.PongMain = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # specifiying server for newtwork
        self.server = "10.240.1.182"

        # specifying port number
        self.port = 5555

        # address for the server.
        self.addr = (self.server, self.port)

        # test code to see if the client and server are connected
        self.pos = self.connect()

    def getPos(self):
        return self.pos


    # Connect function which connects the client to the server.
    def connect(self):
        try:
            self.PongMain.connect(self.addr)
            return self.PongMain.recv(2048).decode()
        except:
            pass

    # Send function which sends data.
    def send(self, data):
        try:
            # encodes data to send
            self.PongMain.send(str.encode(data))

            # receives data and decodes it (receiving 2048 bits)
            return self.PongMain.recv(2048).decode()

        # error
        except socket.error as e:
            print(e)


