import socket, argparse, ipaddress, sys

parser = argparse.ArgumentParser(description="TCP Client connection establish")
parser.add_argument("ip",help="ip to connect")
parser.add_argument("port",type=int, help="port to connect")
parser.add_argument("message", help="message to send")

args=parser.parse_args()

# validate ip address
try:
    ip_object = ipaddress.IPv4Address(args.ip)
    print(f"IP Address is valid: {str(ip_object)}")

except ValueError:
    print(f"Invalid IP Address: {args.ip}")
    sys.exit(1)



sck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sck.connect((args.ip, args.port))
sck.send(args.message.encode())

response = sck.recv(4096)
print(f"Server replied: {response.decode()}")

sck.close()