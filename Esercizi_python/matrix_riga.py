#!/usr/bin/python
# -*- coding: utf-8 -*-

# svrivere un programma python che riceve una matrice quadrata di interi n*n ed un intero e restituisce un vettore di interi contenente per ogni
#riga della matrice il numero di elementi maggiori o uguali all'intero ricevuto
#es. [
#[4,2,3],
#[1,2,1],
#[7,4,5]
# intero=3 e restituisco vettore=[2,0,3]
#modificare la funzione in modo da restituire i valori ottenuti considerando le colonne
#es restituisco vettore=[2,1,2]
# scrivere un programma che riceve una matrice quadrata n*n e restituisce la somma degli elementi sulla diagonale principale
def funzione(matrix, n):
    vector = []
    for i in range(len(matrix)):
        somma = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] >= n:
                somma += 1
        vector.append(somma)
    return vector




def main():
    lista1 = [[4, 2, 3], [1, 2, 1], [7, 4, 5]]
    n = 3
    fun = funzione(lista1, n)
    print(fun)
main()



        