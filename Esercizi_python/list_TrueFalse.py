#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione verifica_liste che riceve una lista L1 di interi e una lista L2 di booleani. La funzione restituisce True se e solo se per tutti gli
# indici i tali che L2[i]==True, la lista L1 non contiene elementi di valore uguale a L1[i] in posizione diversa da i. Esempio: Se L1 = [7, 4, 7, 3, 5, 6] ed
# L2 = [False, True, False, True, True, False], allora la funzione restituisce True perché:  gli indici tali che L2[i]==True sono 1, 3 e 4;  la lista L1
# non contiene elementi di valore uguale a L1[1] (cioè pari a 4) in posizione diversa da 1;  la lista L1 non contiene elementi di valore uguale a L1[3]
# (cioè pari a 3) in posizione diversa da 3;  la lista L1 non contiene elementi di valore uguale a L1[4] (cioè pari a 5) in posizione diversa da 4.

def funzione(lista1, lista2):
    unici = []
    scarti = []
    for elem in lista1:
        if elem not in unici:
            unici.append(elem)
        elif elem not in scarti:
            scarti.append(elem)

    for i in range(len(lista1)):
        if lista2[i] == True and lista1[i] in scarti:
            return False
    return True
            


def main():
    lista1 = [7, 4, 7, 3, 7, 5]
    lista2 = [False, True, False, True, True, False]
    fun = funzione(lista1, lista2)
    print(fun)
main()      

            
        
        