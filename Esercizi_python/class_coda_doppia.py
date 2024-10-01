class Test:
    def __init__(self, lista):
        self.lista = list(lista)

    def addRear(self):
        x = int(input('inserire un numero: '))
        self.lista.insert(0, x)
    def removeRear(self):
        self.lista.pop(0)
    def peekRear(self):
        return self.lista[0]
    def addFront(self):
        x = int(input('inserire un numero: '))
        self.lista.append(x)
    def removeFront(self):
        self.lista.pop()
    def peekFront(self):
        return self.lista[-1]
    def size(self):
        return len(self.lista)
    
        
    def __str__(self):
        stampa = 'Lista: ' + str(self.lista)
        return stampa

def main():
    lista1 = Test([1, 2, 3, 4])
    print(lista1)
    Test.addRear(lista1)
    Test.removeFront(lista1)
    
    print('===============')

    
    print(Test.peekFront(lista1))
    print(lista1)
main()
    

        