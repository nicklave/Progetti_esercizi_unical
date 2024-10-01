#!/usr/bin/python
# -*- coding: utf-8 -*-

# scrivere una funzione che riceve un matrice di interi di dimensioni n * 3 e restituisce il numero di elementi pari a 0 presenti tra la riga di indice i e la riga
# di indice j dove i e j sono passati come parametri alla funzione insieme alla matrice
from random import randint

def printmatrix(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end="  ")
        print()
        
def funzione(matrice, a, b):
    somma = 0
    for i in range(a, b + 1):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 0:
                somma += 1
    return somma

def main():
    n = int(input("Inserisci il numero di righe: "))
    matrice = []
    for i in range(n):
        row = []
        for j in range(3):
            row.append(randint(0, 5))
        matrice.append(row)
            
        
    a = int(input("Inserisci la partenza: "))
    b = int(input("Inserisci l'arrivo: "))
    printmatrix(matrice)
    fun = funzione(matrice, a, b)
    print()
    print(fun)
   


main()





