import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666
s.connect((host, port))
mx = s.recv(1024)
s.close()
print("Server reports the time is {}".format(mx.decode("ascii")))
