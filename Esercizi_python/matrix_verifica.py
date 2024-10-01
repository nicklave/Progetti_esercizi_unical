#!/usr/bin/python
# -*- coding: utf-8 -*-

# Si scriva una funzione verifica che riceve una matrice M di interi e restituisce True se e solo se, per ogni generico
# elemento x = M[i][j], il valore x compare almeno x volte in M.
#Esempio: Se M = [
# 2 5 2 5 5
# 5 3 3 4 3
# 4 2 4 5 4
# ] allora la funzione restituisce True perché il valore 2 è presente 3 volte, il valore 3 è
# presente 3 volte, il valore 4 è presente 4 volte e il valore 5 è presente 5 volte
def contatore(matrix, x):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == x:
                count += 1
    return count
            

def funzione(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a = matrix[i][j]
            if a > contatore(matrix, a):
                return False
    return True
            
            



def main():
    lista1 = [[2, 5, 2, 5, 5], [5, 3, 3, 4, 3 ], [4, 2, 4, 5, 4]]
    fun = funzione(lista1)
    print(fun)
main()



        