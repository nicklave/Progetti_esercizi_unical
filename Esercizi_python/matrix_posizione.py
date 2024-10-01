# scrivere una funzione che riceve una matrice di n righe e m colonne e restituisce il vettore ottenuto nel modo seguente :
# in posizione i del vettore troviamo la somma degli elementi della riga i moltiplicata per la somma degli elementi della colonna 0
# es. 2x3 [[4,5,6],[2,1,6]] restituisce il vettore [15*6,9*6] [90,54]

def restituisci_vettore(matrix):
    vector = []
    somma_colonna = 0
    for i in range(len(matrix)):
        somma = 0
        somma_colonna += matrix[i][0]
        for j in range(len(matrix[i])):
            somma += matrix[i][j]
        vector.append(somma)
    vettore = []
    for i in range(len(vector)):
        vettore.append(vector[i] * somma_colonna)
    print("Il vettore originale e': ", vector)
    print("Il vettore moltiplicato e':  ", vettore)


    
    
def main():
    n = int(input("inserisci l'ordine della matrice quadrata: "))
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            a = int(input("inserisci il numero in posizione [%d,%d]: " % (i, j)))
            row.append(a)
        matrix.append(row)
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="  ")
        print()        

    restituisci_vettore(matrix)

main()