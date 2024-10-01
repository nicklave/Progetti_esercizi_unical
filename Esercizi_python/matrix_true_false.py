#!/usr/bin/python
# -*- coding: utf-8 -*-

# scrivere una funzione in python che riceva una matrice generica n*m di interi e restituisca un vettore di dimensioni m
#contenente nel generico elemento in posizione i il valore True se sulla colonna i è presente almeno uno 0, False altrimenti
#esempio: [3,2,5,7],[4,8,0,2],[0,8,1,3] = [True,False,True,False]
#scrivere un altro metodo che riceva una matrice generica n*m di interi e restituisca un vettore di dimensioni m
#contenente nel generico elemento in posizione i la somma degli elementi sulla colonna i
#esempio: [3,2,5,7],[4,8,0,2],[0,8,1,3] = [7,18,6,12]
def printmatrix(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end="  ")
        print()
        
def funzione(matrice):
    lista = []
    for i in range(len(matrice[0])):
        zero = False
        for j in range(len(matrice)):
            if matrice[j][i] == 0:
                zero = True
        lista.append(zero)

    lista2 = []
    for i in range(len(matrice[0])):
        somma = 0
        for j in range(len(matrice)):
            somma += matrice[j][i]
        lista2.append(somma)
    return (lista, lista2)

def main():
    matrice = [[2, 4, 5], [1, 0, 3], [6, 2, 0]]
    printmatrix(matrice)
    l1,l2 = funzione(matrice)
    print(l1)
    print(l2)
   


main()





