import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7777
ss.bind((host, port))
ss.listen(2)

messages = {}
msgPtr = 1

while True:
    cs, addr = ss.accept()
    print("Connection received from {}".format(str(addr)))
    data = cs.recv(1024)
    messages.update(data, msgPtr)
    cs.send(messages.encode("acii"))
    cs.close()
    msgPtr += 1
