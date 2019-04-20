import socket

TCP_IP = "localhost"
TCP_PORT = 9999
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((TCP_IP, TCP_PORT))
print('Socket bind complete')
s.listen(1)
print('Socket now listening')
print("Waiting for TCP connection...")
print(s.connect())
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))
