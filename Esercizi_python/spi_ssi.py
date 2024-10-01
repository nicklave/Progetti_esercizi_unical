#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione elabora_lista che riceve una lista L1 di interi positivi e restituisce una lista L2 della stessa
#lunghezza di L1, il cui generico elemento L2[i] contiene il massimo tra spi ed ssi, dove spi è la somma degli elementi di
# L1 in posizione precedente a i ed ssi è la somma degli elementi di L1 in posizione successiva a i. Ovviamente, se i = 0 si
# ha spi = 0, mentre se i = len(L1)-1 si ha ssi = 0.
# Esempio: Se L1 = [7, 4, 7, 3, 6, 8], allora la funzione restituisce la lista L2 = [28, 24, 17, 18, 21, 27].

def funzione(lista):
    lista2 = []
    for i in range(len(lista)):
        ssi = 0
        spi = 0        
        for j in range(i + 1, len(lista)):
            ssi += lista[j]
        for k in range(i - 1, -1, -1):
            spi += lista[k]
        if spi > ssi:
            lista2.append(spi)
        else:
            lista2.append(ssi)

    return lista2



def main():
    lista1 = [7, 4, 7, 3, 6, 8]  # [2, 5, 2, 5, 9]
    fun = funzione(lista1)
    print(fun)
main()



        