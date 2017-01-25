import socket

srv = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

srv_ip = socket.gethostbyname(socket.gethostname())
srv_port = 11111
srv.bind((srv_ip , srv_port))
srv.listen(2)
client , ip = srv.accept()
client.send("hii this my first server")
client.close()
hhd=input("press any key t close this cmd line")
                    
