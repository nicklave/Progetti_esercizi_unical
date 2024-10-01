
# Data una matrice quadrata di interi M, un elemento M[i, j] e' detto punto di sella se risulta essere contemporaneamente il minimo
# della riga i e il massimo della colonna j.
# Si scriva una funzione Python punti_di_sella che riceve una matrice quadrata di interi M
# e restituisce una lista di coppie di indici (i,j) che individuano la riga e la colonna in cui si trovano i punti di sella in M (se esistono).

def main():
    lista = [[4, 5, 6],
             [3, 7, 5],
             [2, 4, 3]]
    fun= funzione(lista)
    print(fun)

def funzione(matrix):
    vector = []
    max_colonne = 0
    minimo = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[j][i] > max_colonne:
                max_colonne = matrix[j][i]
                minimo = min(matrix[j])
                k = j
        if minimo == max_colonne:
            vector.append([k, i])
    return vector
            
main()