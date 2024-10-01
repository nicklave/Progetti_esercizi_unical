#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione massimi_sequenze che riceve due interi positivi n e k ed una lista L1 di interi avente lunghezza n * k e restituisce una lista
# L2 di lunghezza k costruita come segue:  consideriamo le n sotto-liste non sovrapposte di k elementi in L1;  l’elemento L2[j] contiene il massimo degli
# elementi che si trovano in posizione j nelle sotto-liste. Esempio: Se n = 4, k = 3 e L1 = [7, 4, 7, 3, 6, 8, 9, 1, 5, 6, 2, 5], allora:  le sottoliste
# non sovrapposte di 3 elementi in L1 sono [7, 4, 7], [3, 6, 8], [9, 1, 5] e [6, 2, 5];  L2[0] = 9 perché gli elementi in posizione 0
# nelle sotto-liste sono 7, 3, 9 e 6;  L2[1] = 6 perché gli elementi in posizione 1 nelle sotto-liste sono 4, 6, 1 e 2;  L2[2] = 8 perché gli elementi
# in posizione 2 nelle sotto-liste sono 7, 8, 5 e 5.

def funzione(lista, n, k):
    lista2 = []
    liss = []
    for i in range(0, len(lista), k):
        listina = []
        for j in range(i, i + k):
            listina.append(lista[j])
        liss.append(listina)
    for i in range(len(liss[0])):
        maximo = 0
        for j in range(len(liss)):
            if liss[j][i] > maximo:
                maximo = liss[j][i]
        lista2.append(maximo)
            
    print(liss)
    return lista2


def main():
    lista1 = [7, 4, 7, 3, 6, 8, 9, 1, 5, 6, 2, 5]
    n = 4
    k = 3
    fun = funzione(lista1, n, k)
    print(fun)
main()



        