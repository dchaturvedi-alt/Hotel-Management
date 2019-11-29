import socket
import time
# import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1241))
s.listen(5)
print("kuch toh ho raha hai")
while True:
	try:
		clt, adr = s.accept()
		print(f"Connection to {adr} established")
		print(clt, adr)
		clt.send(bytes("connection ho gaya re baba", "utf-8"))
		# clt.recv(1024)
        # time.sleep(10)
		clt.send(bytes("quit", "utf-8"))
		print("endl")
	except:
		s.close()
