#!/usr/bin/python
# -*- coding: utf-8 -*-

# svrivere un programma python che riceve una matrice quadrata di interi n*n ed un intero e restituisce un vettore di interi contenente per ogni
#riga della matrice il numero di elementi maggiori o uguali all'intero ricevuto
#es. [
#[4,2,3],
#[1,2,1],
#[7,4,5]
#]
#intero=3 e restituisco vettore=[2,0,3]
#modificare la funzione in modo da restituire i valori ottenuti considerando le colonne
#es restituisco vettore=[2,1,2]
# scrivere un programma che riceve una matrice quadrata n*n e restituisce la somma degli elementi sulla diagonale principale


def printmatrix(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end="  ")
        print()
        
def funzione(matrix, intero):
    vector = []
    for i in range(len(matrix)):
        somma = 0
        for j in range(len(matrix[i])):
            if matrix[j][i] >= intero:
                somma += 1
        vector.append(somma)
    return vector
def main_diag(matrice):
    somm = 0
    for i in range(len(matrice)):
        somm += matrice[i][i]
    return somm

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
    fun = funzione(matrice, 2)
    print(fun)
    fu = main_diag(matrice)
    print(fu)


main()





