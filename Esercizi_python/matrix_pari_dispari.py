# scrivere una funzione in python che riceva in ingresso una matrice quadrata n*n di interi e restituisca un vettore di dimensioni n contenente
# in posizione i:  il valore massimo sulla colonna i, se i e' pari; il valore minimo sulla colonna i, se i e' dispari(lo 0 e' considerato pari)
#ES:[ 4 3 2 ] [ 8 1 7 ] [ 5 1 7 ] | RESTITUISCO [ 8,1,7 ]
# si consideri la versione piu' semplice della quale il metodo restituisce un vettore di dimensioni n contenente in posizione i il valore massimo sulla colonna i
# ES:[ 4 3 2 ] [ 8 1 7 ] [ 5 1 7 ] | RESTITUISCO [ 8,3,7 ]

def main():
    lista = [[4, 3, 2], [8, 1, 7], [5, 1, 7]]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end="  ")
        print()
    print()
    print(funzione(lista))

def funzione(matrix):
    vector = []
    for i in range(len(matrix)):  # i = 0
        x = matrix[0][0]
        for j in range(len(matrix)):  # j = 0
            if i % 2 == 1:
                if matrix[j][i] < x:
                    x = matrix[j][i]
            else:
                if matrix[j][i] > x:
                    x = matrix[j][i]
        vector.append(x)
    return vector


main()
            

            
    
