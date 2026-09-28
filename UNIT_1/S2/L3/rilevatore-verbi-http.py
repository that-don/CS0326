import http.client

host = input("Inserire host/IP del sistema target: ")
input_port = input("Iserisci la porta del sistema target (default 80): ")
metodi = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH']

port = int(input_port) if input_port else 80 

for metodo in metodi:

    try:
        conn = http.client.HTTPConnection(host, port)
        conn.request(metodo, '/')
        response = conn.getresponse()
        
        # Modifiche per stampare informazioni utili
        print(f"\nStato: {response.status} {response.reason}")
        print("\nHeader della risposta:")
        for header, value in response.getheaders():
            print(f"{header}: {value}")
            
        conn.close()

    except ConnectionRefusedError:
        print('Connessione fallita: il server non è raggiungibile o la porta è chiusa.')