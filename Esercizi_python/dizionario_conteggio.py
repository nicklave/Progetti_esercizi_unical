# scrivere un funzione in python che riceva in ingresso una lista di stringhe e restisuisca
#un dizionario contenente per ciascuna stringa il numero di occorrenze nella lista ricevuta
#la coppia costituita dalla stringa piu' frequente e dalla stringa meno frequente
#se esistono dei pari merito si lascia libera la scelta della loro gestione
#es. lista = ["cane", "casa", "rosa", "casa", "casa", "rosa"] == ("casa", "cane")
def funzione(lista):
    dizionario = {}

    for elem in lista:
        if elem in dizionario:
            dizionario[elem] += 1
        else:
            dizionario[elem] = 1

    max_freq = 0
    key0 = ''
    key1 = ''
    for elem in dizionario:
        if dizionario[elem] > max_freq:
            max_freq = dizionario[elem]
            key1 = elem

    min_freq = max_freq
    for elem in dizionario:
        if dizionario[elem] < min_freq:
            min_freq = dizionario[elem]
            key0 = elem        
    print(key0, key1)

        
    for elem in sorted(dizionario):
        print(elem, ':', dizionario[elem])


