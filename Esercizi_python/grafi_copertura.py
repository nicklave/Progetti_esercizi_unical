def minimoScore(g):
    minimo = 6
    for i in range(len(g)):
        count = 0
        for j in range(len(g)):
            if g[j][i] == 1 and (j + 1) % 2 == 0:
                count += 1
        if count < minimo:
            minimo = count
    return minimo


def copertura(g, l):
    for i in l:
        for j in l:
            if i != j:
                if g[i - 1][j - 1] == 0 and g[j - 1][i - 1] == 0:
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
    print(minimoScore(matrice))
    l = [1, 2, 4, 6]
    print(copertura(matrice,l))
    
main()