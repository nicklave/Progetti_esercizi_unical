def massimoScore(g):
    massimo = 0                          # 1
    for i in range(len(g)):              # n
        count = 0                          # n-1
        for j in range(len(g)):            # sum (1,n-1) di t
            if (j + 1) % 2 != 0 and g[j][i] == 1:  # sum (1,n-1) t-1
                count += 1                # sum (1,n-1) t-1
        if count > massimo:
            massimo = count
    return massimo

def speciale(g, x):
    for i in range(len(g)):
        if g[x - 1][i] == 1 and (i + 1) % 2 == 1:
            return False
    return True

def lista_speciale(g, l):
    for i in l:
        if not speciale(g, i):
            return False
    return True


def main():
#               1  2  3  4  5  6
    matrice = [[0, 1, 1, 1, 0, 0],  # 1
               [0, 0, 1, 0, 0, 0],  # 2
               [0, 0, 0, 0, 0, 0],  # 3
               [0, 1, 1, 0, 0, 1],  # 4
               [0, 1, 0, 1, 0, 1],  # 5
               [0, 0, 0, 0, 0, 0]]  # 6
    
    print('score massimo: ', massimoScore(matrice))
    lista = [3, 1]
    print('I nodi della lista: ', lista, ' sono speciali? ', lista_speciale(matrice, lista))
main()

               