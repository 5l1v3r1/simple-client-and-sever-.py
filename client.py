import socket

cli = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())

port = 11111

cli.connect((ip , port))
server_reply = cli.recv(65439)
print server_reply
cli.close()
osdi=input("pres enetr t close")
