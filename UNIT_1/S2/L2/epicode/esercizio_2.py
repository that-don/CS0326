# SCRIVI UN PROGRAMMA CHE CHIEDA 3 NUMERI ALL'UTENTE E CALCOLI LA LORO MEDIA


def inserimento():
    lista = []
    counter = 1
    print("inserisci 3 numeri")
    while True:
        try: 
            num = float(input(f"{counter}° numero: "))            
            lista.append(num)
            if counter == 3:
                return lista
            counter += 1
            
        except:
            print("inserisci un valore valido")

def calcolo():
  lista = inserimento()
  sum = 0
  for element in lista:
      sum += element
  
  media = sum / len(lista)
  return lista, media
    
def main():
    lista, media = calcolo()
    print("hai inserito i numeri:")
    for element in lista:
        print(element)
    print(f"la loro media è {media:.2f}")


main()