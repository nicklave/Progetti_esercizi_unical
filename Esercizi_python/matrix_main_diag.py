# scrivere una funzione python che riceve una matrice quadrata n*n di numeri reali
#e restituisce un vettore composto da tre elementi
#il primo elemento contiene la somma degli elementi della matrice al di sotto della diagonale principale
#il secondo elemento contiene il numero di elementi maggiori di 10 presenti nella matrice
#il terzo elemento contiene il prodotto degli elementi sulla diagonale principale della matrice
#es. matrice = [[4, 5, 20],
# [2, 1, 15],
# [5, 3, 4]] ----- vettore = [10, 2, 16]
def main():
    matrix = [[2, 3, 4], [1, 5, 7], [9, 4, 2]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="  ")
        print()
    fun = funzione(matrix)
    print(fun)

def funzione(matrix):
    somma = 0
    vector = []
    n = 0
    prod = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 10:
                n += 1
            if j < i:
                somma += matrix[i][j]
            if i == j:
                prod *= matrix[i][j]
    vector.append(somma)
    vector.append(n)
    vector.append(prod)

    return vector
    
main()