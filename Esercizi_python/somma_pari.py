# scrivere una funzione in python che riceva una lista di interi e restituisca la somma degli interi pari in posizione dispari
#ex: [4,2,6,3,5,8,7] __ 2+8=10
#la media
from random import randint

def funzione(lista):
    somma = 0
    n = 0
    for i in range(len(lista)):
        if i % 2 == 1 and lista[i] % 2 == 0:
            somma += lista[i]
    return somma

def main():
    lista123 = [4, 2, 6, 3, 5, 8, 7]


    print()
    fun = funzione(lista123)
    print(fun)
    
main()
        
    