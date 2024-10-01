#!/usr/bin/python
# -*- coding: utf-8 -*-

# scrivere una funzione python che riceve una matrice quadrata n*n di numeri reali
# e restituisce un vettore composto da tre elementi
# il primo elemento contiene la somma degli elementi della matrice al di sotto della diagonale principale
# il secondo elemento contiene il numero di elementi maggiori di 10 presenti nella matrice
# il terzo elemento contiene il prodotto degli elementi sulla diagonale principale della matrice
# es. matrice = [[4, 5, 20],
# [2, 1, 15],
# [5, 3, 4]] ----- vettore = [10, 2, 16]
def printmatrix(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end="  ")
        print()
        
def funzione(matrice):
    vector = []
    num = 0
    somma = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if j < i:
                somma += matrice[i][j]
            if matrice[i][j] > 10:
                num += 1

    prod = 1
    for i in range(len(matrice)):
        prod *= matrice[i][i]
    vector.append((somma, num, prod))
    return(vector)

    
        



def main():
    n = int(input("inserisci l'ordine della matrice quadrata: "))

    matrice = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            a = int(input("inserisci il numero in posizione [%d,%d]: " % (i, j)))
            row.append(a)
        matrice.append(row)
    printmatrix(matrice)
    fun = funzione(matrice)
    print(fun)
   


main()





