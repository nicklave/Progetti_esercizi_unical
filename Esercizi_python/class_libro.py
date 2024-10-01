class CatalogoLibri:

    def __init__(self):
        self.diz = {}

    def aggiungiLibro(self, libro, autori):
        if libro not in self.diz:
            self.diz[libro] = autori
            return True
        else:
            return False

    def eliminaLibro(self, libro):
        if libro in self.diz:
            self.diz.pop(libro)
            return True
        else:
            return False

    def aggiungiAutore(self, libro, autore):
        if libro in self.diz and autore not in self.diz[libro]:
            self.diz[libro].append(autore)
            return True
        else:
            return False

    def eliminaAutore(self, libro, autore):
        if libro in self.diz and autore in self.diz[libro]:
            self.diz[libro].remove(autore)
            return True
        else:
            return False

    def autore(self, persona):
        for libro in self.diz:
            if persona in self.diz[libro]:
                return True
        return False

    def lista_libri(self):
        lista = []
        for libro in self.diz:
            for autore in self.diz[autore]:
                if autore not in lista:
                    lista.append(autore)
        return lista
    
    def libriScritti(self, persona):
        lista = []
        for libro in self.diz:
            if persona in self.diz[libro] and libro not in lista:
                lista.append(libro)
        return lista

    def __repr__(self):
        s = ""
        for libro in self.diz:
            s = s + "Il libro '" + libro + "' e' stato scritto dai seguenti autori : " + str(self.diz[libro]) + "\n"
        return s
    
    def NumeroMassimoAutori(self):
        massimo = 0
        for libro in self.diz:
            if len(self.diz[libro]) > massimo:
                massimo = len(self.diz[libro])
        return massimo


def main():
    
    Biblioteca = CatalogoLibri()
    
    Biblioteca.aggiungiLibro("1984", [])
    Biblioteca.aggiungiLibro("Numeri", [])
    Biblioteca.aggiungiLibro("ciao", [])
    
    #Biblioteca.aggiungiAutore("1984", "peppino")
    Biblioteca.aggiungiAutore("1984", "peppe")
    Biblioteca.aggiungiAutore("1984", "peppi")
    Biblioteca.aggiungiAutore("Numeri", "peppino")
    Biblioteca.aggiungiAutore("ciao", "peppino")
    

    print(Biblioteca)
    print(Biblioteca.autore("peppe"))
    print(Biblioteca.libriScritti("peppino"))
    print(Biblioteca.NumeroMassimoAutori())
    
main() 
        
                    