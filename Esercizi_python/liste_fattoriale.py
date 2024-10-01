n = int(input("inserisci il numero di elementi:"))
lista_01 = []

for i in range(0, n + 1):
    if i % 2 == 0:
        lista_01.append(i)

print("I numeri pari fino ad n incluso sono:", lista_01)
lista_02 = []
for i in range(5):
    x = int(input("Inserisci un numero da aggiungere alla lista: "))
    lista_02.append(x)
    print(lista_02)

fatt=int(input("Inserisci il numero di cui calcolare il fattoriale: "))
def Fattoriale(n):
    fact = 1
    k = 1
    while k <= n:
        fact = fact * k
        k += 1
    return (fact)


print(Fattoriale(fatt))


def esamina_lista(n):
    for i in range(0, len(n)):
        x = n[i]
        x_01 = n[-i - 1]
        x_tot = x + x_01
        if x_tot > sum(n[i + 1:-i - 1]):
            y = "true"
        else:
            y = "false"
        print(n)
       
        return (y)

print(esamina_lista(lista_02))

