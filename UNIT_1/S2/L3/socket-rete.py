# CREAZIONE SEMPLICE DI UN SOCKET DI RETE

import socket

SRV_ADDR = "192.168.64.6" #indirizzo di questo pc che ascolta
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
s.bind((SRV_ADDR, SRV_PORT)) # binding = collegamento tra socket e indirizzo che abbiamo scelto
s.listen(1) # backlog = 1 = connessioni massime in coda
print("Server started! waiting for connection...")

connection, address = s.accept()
# connessione = <socket.socket fd=4, family=2, type=1, proto=0, laddr=('192.168.64.6', 44444), raddr=('192.168.64.6', 38512)>
# indirizzo = ('192.168.64.6', 38512)

print(f"Client connected with address: {address}")
while True:
    data = connection.recv(1024) # 1024 = dimensione del buffet in byte
    if not data: break
    connection.send(b'--Messaggio ricevuto--\n')
    print(f"messaggio ricevuto: {data.decode("utf-8")}")
connection.close()