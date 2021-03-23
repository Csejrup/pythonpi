import socket
HOST = '192.168.87.133'  # Server IP
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("Enter a Message: ")
    s.send(message)
   # s.sendall(b''+message)
    data = s.recv(1024)

print('Received', repr(data))


