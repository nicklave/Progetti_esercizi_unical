def massimoScore(g):
    massimo = 0
    for i in range(len(g)):
        count = 0
        for j in range(len(g[i])):
            if g[i][j] % 2 == 0:
                count += 1
        if count > massimo:
            massimo = count
    return massimo

def cricca(G, l):
    # [1,2,3,4]
    for i in l:
        for j in l:
            if i != j:
                if j not in G[i - 1] and i not in G[j - 1]:
                    return False
    return True
    
    
def main():
    lista_adiacenze = [[2, 3, 4],
                       [3],
                       [],
                       [2, 3, 6],
                       [2, 4, 6],
                       []]
    lista = [1, 2, 5]
    for i in range(len(lista_adiacenze)):
        print(i + 1, '->', lista_adiacenze[i], end='')
        print()
    print('massimo score: ', massimoScore(lista_adiacenze))
    print('la lista ', lista, 'e una cricca?', cricca(lista_adiacenze,lista))
main()
