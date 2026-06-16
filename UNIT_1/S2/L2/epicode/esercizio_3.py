# SCRIVI UN NUMERO CHE CHIEDA UN NUMERO ALL'UTENTE E STAMPI LA SUA TABELLINA FINO A 10

def scelta_utente():
    while True:
        try:
            num = int(input("inserisci un numero intero: "))
            return num
        except:
            print("inserisci un numero valido")

def tabellina():
    num = scelta_utente()
    for _ in range(11):
        print(f"{num} * {_} = {num * _}")

tabellina()
