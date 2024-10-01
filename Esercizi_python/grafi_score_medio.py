def scoreMedio(g):
    somma = 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] % 2 == 0:
                somma += 1
    media = somma / len(g)
    return media

def speciale(g, i):
    for j in range(1, len(g) + 1):
        if i in g[j - 1] and j % 2 == 0:
            return False
    return True

def nessunSpeciale(g, l):
    for i in l:
        if speciale(g, i):
            return False
    return True

def main():
    lista_adiacenze = [[2, 3, 4],
                       [3],
                       [],
                       [2, 3, 6],
                       [2, 4, 6],
                       []]
    l = [2, 6]

    for i in range(len(lista_adiacenze)):
        print(i + 1, '->', lista_adiacenze[i], end='')
        print()
    print()
        
    print(scoreMedio(lista_adiacenze))
    print(nessunSpeciale(lista_adiacenze, l))
    

main()