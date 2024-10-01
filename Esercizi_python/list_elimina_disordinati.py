#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione filtra_ordinati che riceve una lista L1 di interi e restituisce una lista L2 ottenuta a partire da L1
#eliminando tutti gli elementi che ne violano l’ordinamento crescente. In altri termini, un elemento di L1 dev’essere
# inserito in L2 se e solo se è maggiore di tutti gli elementi che lo precedono in L1.
#Esempio: Se L1 = [1, 2, 5, 4, 7, 8, 3, 9] allora filtra_ordinati(L1) restituisce la lista L2 = [1, 2, 5, 7, 8, 9].
def funzione(lista):
    lista2 = []
    for i in range(len(lista)):
        if i == 0:
            lista2.append(lista[i])
        elif lista[i] > ultimo(lista2):
            lista2.append(lista[i])
    return lista2

def ultimo(lista):
    return lista [- 1]




def main():
    lista1 = [1, 2, 5, 4, 7, 8, 3, 9]  # [5, 4, 6, 3, 6, 8, 9, 1]  # [7, 4, 7, 3, 6, 8, 9, 1, 5, 6, 2, 5]

    print(lista1[-1])
    
    
    
main()



        