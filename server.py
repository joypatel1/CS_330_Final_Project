# https://www.youtube.com/watch?v=_whymdfq-R4 - Youtube Toutorial on how to create a server in python.
import socket
from _thread import *
import sys

# Locol server address
server = "10.240.1.182"

# port used to connect
port = 5555

# socket setup with types of connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # binding server and port to look for server
    s.bind((server, port))
except socket.error as e:
    str(e)

# listening for connections
s.listen()
print("Please wait to be connected to the server.")


# threading function
def threaded_client(conn):
    pass
    reply = ""

    # continously looking for new connection.
    while True:
        try:
            # recieving data from connection specified as bits
            data = conn.recv(2048)

            # decoding data
            reply = data.decode("utf-8")

            # disconnects user if there is no data to stop infinite loops
            if not data:
                print("Disconnected")
                break

            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            #encodes data into bytes
            conn.sendall(str.encode(reply))

        except:
            break


while True:
    # accepting new connections
    conn, addr = s.accept()
    print("Succefully connected to:", addr)

    # create new thread
    start_new_thread(threaded_client, (conn,))
