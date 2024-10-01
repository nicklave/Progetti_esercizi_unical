class carrello:

    def __init__(self):
        self._carrello = {}

    def aggiungi(self, nome, quantita=1):
        if nome in self._carrello:
            self._carrello[nome] += quantita
        else:
            self._carrello[nome] = quantita

    def visualizza(self, nome):
        if nome in self._carrello:
            return self._carrello[nome]
        else:
            return 0
    
    def elimina(self, nome):
        if nome in self._carrello:
            self._carrello.pop(nome)
    
    def svuota(self):
        self._carrello = {}

    def get_nome(self):
        return self._carrello.items()

    def __repr__(self):
        stringa = 'IL carrello contiene: \n'
        for (nome, quantita) in self._carrello.items():
            stringa += str(quantita) + ' ' + nome + '\n'
        return stringa

def main():
    c1 = carrello()
    c1.aggiungi('banana', 2)
    c1.aggiungi('pera')
    print(c1.visualizza('pera'))
    print(c1.get_nome())


main()
