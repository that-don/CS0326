import socket

target = input("inserisci l'indirizzo IPv4: ")
portrange = input("inserisci il range delle porte (es. 50-200): ")

lowport = int(portrange.split('-')[0])
hihgport = int(portrange.split('-')[1])

print(f"Scanning host {target} from port {lowport} to {hihgport}")

for port in range(lowport,hihgport+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print(f"Port {port} - OPEN")
    else:
        print(f"Port {port} - CLOSED")
    s.close()