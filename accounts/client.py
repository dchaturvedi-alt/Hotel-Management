import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1241))

full_msg = ''
while True:
    print("message start")
    msg = s.recv(8)
    print(msg.decode("utf-8"))
    if(msg.decode("utf-8").find("quit")>=0 or len(msg)<=0):
        break
    full_msg += msg.decode("utf-8")
print(full_msg)

