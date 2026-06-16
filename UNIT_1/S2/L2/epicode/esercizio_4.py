# Scrivi un programma che chieda una stringa e conti il numero di vocali presenti

def inserisci_stringa():
    stringa = input("scrivi qualcosa: ").lower()
    return stringa

def controllo():
    stringa = inserisci_stringa()
    vocali = ['a','e','i','o','u']
    counter = 0
    for lettera in stringa:
        if lettera in vocali:
            counter += 1
    
    return stringa, counter

def main():
    stringa, counter = controllo()
    print(f"hai scritto {stringa} con {counter} vocali")

main()