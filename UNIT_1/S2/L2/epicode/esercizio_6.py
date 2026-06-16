# Scrivi un programma che chieda una stringa e la stampi al contrario. 

def inserisci_stringa():
    stringa = input("scrivi qualcosa: ")
    return stringa

def main():
    stringa = inserisci_stringa()
    print(stringa[::-1])

main()