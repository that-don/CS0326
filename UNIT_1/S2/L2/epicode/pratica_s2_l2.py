"""
In questo esercizio, dovrai creare un programma che esegue le seguenti operazioni: 
Richiesta di Input: Il programma deve chiedere all'utente di inserire: 
- Il nome della città di origine.-
- Il nome del proprio animale domestico. 
Generazione del Nome della Band: Una volta ricevuti gli input.

il programma deve combinare il nome della città e il nome dell'animale in un'unica stringa che rappresenta il nome della band.

Output: Il programma deve stampare a video il nome generato per la band.
"""

def scelta_nome():
  citta = input("inserisci il nome della tua città: ").strip().lower()
  animale = input("inserisci il nome del tuo animale domestico: ").strip().lower()
  return citta, animale

def crea_nome_band():
  citta, animale = scelta_nome()
  nome_band = f"{citta}{animale}".capitalize()
  print(f"il nome della band sarà {nome_band}")

crea_nome_band()