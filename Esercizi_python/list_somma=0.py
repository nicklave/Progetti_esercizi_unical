#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione verifica_sequenza che riceve una lista L di interi e un intero k e restituisce True se e solo se la
#lista contiene k elementi consecutivi la cui somma è pari a zero.
# Esempio: Se L = [6, 1, -5, 3, 1, -5, -1, 9] e k = 4, allora verifica_sequenza(L,k) restituisce True perché L contiene 4 elementi
#consecutivi (1, -5, 3 e 1) la cui somma è pari a zero

def funzione(lista, k):
    for i in range(len(lista) - k + 1):
        temp = lista[i]
        for j in range(i + 1, k + i):
            temp += lista[j]
            
        if temp == 0:
            return True
    return False



def main():
    lista1 = [2, 5, 2, 5, 9, -5, -3, -2, 6, 7, -8]
    fun = funzione(lista1, 4)
    print(fun)
main()



        