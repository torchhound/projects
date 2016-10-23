import socket

host = socket.gethostname()
port = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    sent = input("say: ")
    s.connect((host, port))
    s.sendall(sent)
    received = s.recv(1024)
    s.close()
    print(received.decode("ascii") + "\n")
