import socket

sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sv.bind(("127.0.0.1",9999))
sv.listen(5)

print("Server is listening on port 9999")

client_socket, client_addr = sv.accept()
data = client_socket.recv(1024)
client_socket.send(b"Hey there client!, This is server.")
client_socket.close()