# scrivere una funzione in python che riceva una lista di interi e restituisca il secondo massimo

def funzione(lista):
    massimo = 0
    for elem in lista:
        if elem > massimo:
            massimo = elem
    lista.remove(massimo)
    massimo2 = 0
    for elem in lista:
        if elem > massimo2:
            massimo2 = elem
    return massimo2
   
def main():
    lista = [5, 4, 54, 5, 4, 788, 9, 7]
    print(funzione(lista))
main()