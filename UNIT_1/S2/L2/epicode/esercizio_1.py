# SCRIVI UN PROGRAMMA CHE CHIEDA UN NUMERO ALL'UTENTE E DETERMINI SE E' PARI O DISPARI

# il programma prevede la separazione delle fasi per una maggiore scalabilità
def scelta_utente():

    # il ciclo infinito serve a mantenere la domanda fino a quando l'utente non inserisce il valore giusto
    while True:
        try:
            # la conversione avviene per far si che il programma lanci un errore in caso di input sbagliato
            num = float(input("inserisci un numero: "))
            return num
        except:
            print("inserisci un numero valido")


def controllo():
    num = scelta_utente()
    if num % 2 == 0:
        print(f"hai scelto {num} ed è un numero pari") 
    else:
        print(f"hai scelto {num} ed è un numero disppari")


def main():
    controllo()

if __name__ == "__main__":
    main()
