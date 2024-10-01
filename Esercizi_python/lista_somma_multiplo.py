# scrivere una funzione python che riceva una lista di interi e restituisca una lista contenente gli interi
# ottenuti moltiplicando ciascun elemento, per la somma degli elementi della lista se l'elemento
# e multiplo di 3, s e l'elemento non e multiplo di 3 si inserir in lista l'elemento stesso
# es lista= [3,5,4,9,1,0,3] somma elementi= 25
#risultato= [ 75, 5,4,225, 1,0, 75]
from random import randint

def funzione(lista):
    somma = 0  # 1
    lista2 = []  # 1
    for i in range(len(lista)):  # n
        somma += lista[i]
    print('La somma e: ', somma)  # 1
    for i in range(len(lista)):  # 4n
        if lista[i] % 3 == 0:
            lista2.append(lista[i] * somma)
        else:
            lista2.append(lista[i])
    return lista2

def main():
    lista = []
    for i in range(5):
        lista.append(randint(0, 10))
    print(lista)
    print()
    fun = funzione(lista)
    print(fun)
    
main()
        
    