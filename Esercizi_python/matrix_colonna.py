# Scrivere una funzione in python che riceva in ingresso una matrice quadrata n*n di interi
# e restituisca un vettore di dimensioni n contenente nel generico elemento in pos i
# il valore true se sulla colonna i e' presente il numero 8
# false altrimenti
# Es [3,2,5] vettore = [false, true true]
#   [4,8,8]
#   [0,8,1]
def main():
    matrix = [[2, 3, 1], [1, 5, 8], [3, 8, 2]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="  ")
        print()
    fun = funzione(matrix)
    print(fun)

def funzione(matrix):
    vector = []
    for i in range(len(matrix[0])):
        x = False
        for j in range(len(matrix)):
            if matrix[j][i] == 8:
                x = True
        vector.append(x)
    return vector

main()
