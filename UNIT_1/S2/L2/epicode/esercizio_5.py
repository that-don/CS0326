# SCRIVI UN PROGRAMMA CHE CHIEDA ALL'UTENTE UNA LISTA DI NUMERI E TROVI IL MASSIMO

def scelta_utente():
    lista = []
    while True:
        try:
            num = float(input("inserisci un numero (-1 per terminare): "))
            if num == -1:
                return lista
            lista.append(num)
        except:
            print("inserisci un numero valido")

def main():
    lista = scelta_utente()
    print(f"il valore più grande che hai inserito è {max(lista)}")

main()