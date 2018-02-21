import socket
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666
serverSocket.bind((host, port))
serverSocket.listen(3)

while True:
    clientSocket, addr = serverSocket.accept()
    print("Connection received from {}".format(str(addr)))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientSocket.send(currentTime.encode("ascii"))
    clientSocket.close()
