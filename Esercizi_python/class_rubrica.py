class rubrica:
    
    def __init__(self):
        self._contatto = {}

    def creaContatto(self, nome):
        if nome not in self._contatto:
            self._contatto[nome] = []
            return True
        else:
            return False

    def eliminaContatto(self, nome):
        if nome in self._contatto:
            self._contatto.pop(nome)
            return True
        else:
            return False

    def aggiungiNumero(self, nome, numero):
        if nome in self._contatto and numero not in self._contatto[nome]:
            self._contatto[nome].append(numero)
            return True
        else:
            return False
            
        

    def cercaNumeri(self, nome):
        if nome in self._contatto:
            return self._contatto[nome]
        else:
            return None

    def svuotaRubrica(self):
        self._contatto = {}

    def __repr__(self):
        stringa = 'Contatti in rubrica: \n'
        for (nome, contatti) in self._contatto.items():
            stringa += nome + str(contatti) + '\n'
        return stringa

    def verificaContattiConStessoNumero(self):
        lista_contatti = []
        for nome in self._contatto:
            if self._contatto[nome] not in lista_contatti:
                lista_contatti.append(self._contatto[nome])
            else:
                return True
        return False

def main():
    c1 = rubrica()
    c1.creaContatto('nick')
    c1.creaContatto('deb')
    c1.aggiungiNumero('nick', 1234)
    c1.aggiungiNumero('deb', 3456)
    print(c1.verificaContattiConStessoNumero())
    print(c1)

main()





