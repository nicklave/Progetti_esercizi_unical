# scrivere una funzione in python che riceve una lista di stringhe
#e restituisca un dizionario contenente per ogni stringa il numero di occorenze in lista solo se tale numero e maggiore di 1
# ex: ["cane","casa","rosa","casa","casa","rosa"]----[casa:3 , rosa:2]
#restituire una lista contenente solo le stringhe che compaiono nella lista ricevuta piu di una volta
#ex:["cane","casa","rosa","casa","casa","rosa"]----[casa, rosa]
#restituisca la stringa piu frequente
# ex:["cane","casa","rosa","casa","casa","rosa"]----casa

def funzione(lista):
    dizionario = {}

    for elem in lista:
        if elem in dizionario:
            dizionario[elem] += 1
        else:
            dizionario[elem] = 1
    lista = []

    for elem in lista:
        if dizionario[elem] == 1:
            dizionario.pop(elem)
    print(dizionario)



def main():
    lista = ["cane", "casa", "rosa", "casa", "casa", "rosa"]
    funzione(lista)
    
main()
