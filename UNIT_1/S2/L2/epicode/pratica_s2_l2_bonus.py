# Esercizio 1: 
# Calcolo della media mobile Esercizio Python per Hacker Descrizione: 
# Scrivi una funzione che calcoli la media mobile di una lista di numeri. 
# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.


def calcolo_media_mobile():
    lista = [1,2,3,4,5,6,7,8,9,10]
    n = 3
    media_mobile = sum(lista[len(lista) - n : len(lista)]) / n
    print(media_mobile)

calcolo_media_mobile()


# Esercizio 2: 
# Analisi delle Esercizio Python per Hacker parole Scrivi una funzione che analizzi una stringa di testo e 
# restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola. 
# Ignora la punteggiatura e considera le parole in modo case-insensitive.

import re

def qunatita_parole():
    stringa = input("inserisci una frase: ").lower()
    stringa_pulita = re.sub(r"[^\w\s]", "", stringa)
    lista_parole = stringa_pulita.split()
    obj = {}
    for parola in lista_parole:
        obj[parola] = obj.get(parola, 0) + 1
    
    print(obj)
      
qunatita_parole()