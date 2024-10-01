from random import randint

N_INTERI = 10

lista = []

for i in range(N_INTERI):
    n_random = randint(0, 10)
    lista.append(n_random)
print(lista)

print("elementi con indice pari: ", end="")

for i in range(0, N_INTERI, 2):
    print(lista[i], end=", ")
print()


def reverse(lista):
    for i in range(0, len(lista) // 2):
        temp = lista[i]
        lista[i] = lista[len(lista) - 1 - i]
        lista[len(lista) - 1 - i] = temp

print(lista)
reverse(lista)
print(lista)

def reverse_01(lista):
    for i in range(0, len(lista) // 2):
        j = len(lista) - 1 - i
        temp = lista [i]
        lista[i] = lista[j]
        lista[j] = temp

print(lista)
reverse_01(lista)
print(lista)





