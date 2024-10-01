# scrivere una funzione python che riceva una lista di stringhe e restituisca un vettore contenente tre elementi
#il primo elemento contiene il numero di stringhe con lunghezza superiore ai tre caratteri il secondo
#elemento contiene la stringa piu corta presente in lista e il terzo elemento contiene il numero di stringhe presenti una sola volta in lista
#ex:[cane,casa,rosa,casa,pio,mio,si,zio,pio] risultato=[4,"si",5]
def main():
    lista = ['cane', 'casa', 'rosa', 'casa', 'pio', 'mio', 'si', 'zio', 'pio']
    fun = funzione(lista)
    print(fun)


def funzione(lista):
    vector = []
    x = 0
    n = 0
    parole = []
    scarti = []
    min_string = lista[0]
    for i in range(len(lista)):
            if len(lista[i]) > 3:
                n += 1
            if len(lista[i]) < len(min_string):
                min_string = lista[i]
    for elem in lista:
        if elem not in parole:
            parole.append(elem)
        elif elem not in scarti:
            scarti.append(elem)
    x += (len(parole) - len(scarti))


    
    vector.append(n)
    vector.append(min_string)
    vector.append(x)
    
    return vector
                       


main()
