
def quadrati_perfetti(n):
    i = 0
    lista = []
    while i < n:
        x = i**2
        if x <= n:
            lista.append(x)
        i += 1
    return lista

def divisibili_per_10(n):
    i = 0
    lista = []
    while i <= n:
        if i % 10 == 0:
            lista.append(i)
        i += 1
    return lista

def potenze_di_2(n):
    i = 0
    lista = []
    while i <= n:
        if 2**i <= n:
            lista.append(2**i)
        i += 1
    return lista

def main():
    pippo = int(input("Digita un numero: "))
    print(quadrati_perfetti(pippo))
    print(divisibili_per_10(pippo))
    print(potenze_di_2(pippo))
main()

