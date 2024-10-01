class PianiDiStudi:

    def __init__(self):
        self._diz = {}


    def aggiungiStudente(self, matricola):
        insieme = set()
        if matricola not in self._diz:
            self._diz[matricola] = insieme
            return True
        else:
            return False

    def eliminaStudente(self, matricola):
        if matricola in self._diz:
            self._diz.pop(matricola)
            return True
        else:
            return False
    def aggiungiInsegnamentoalPiano(self, matricola, insegnamento):
        if matricola in self._diz and insegnamento not in self._diz[matricola]:
            self._diz[matricola].add(insegnamento)
            return True
        else:
            return False
    def eliminaInsegnamentoDalPiano(self, matricola, insegnamento):
        if matricola in self._diz and insegnamento in self._diz[matricola]:
            self._diz[matricola].remove(insegnamento)
            return True
        else:
            return False
        
    def insegnamentoSceltoDaNessuno(self, insegnamento):
        for matricola in self._diz:
                if insegnamento in self._diz[matricola]:
                    return False
        return True

    
    def insegnamentiSceltiDaTutti(self):
        lista_insegnamenti = []

        for matricola in self._diz:
            for insegnamento in self._diz[matricola]:
                if insegnamento not in lista_insegnamenti:
                    lista_insegnamenti.append(insegnamento)
                    
        for matricola in self._diz:
            for insegnamento in lista_insegnamenti:
                if insegnamento not in self._diz[matricola]:
                    lista_insegnamenti.remove(insegnamento)
            insieme = set(lista_insegnamenti)
        return insieme

    def __repr__(self):
        stringa = ''
        for (matricola, insegnamenti) in self._diz.items():
            stringa += 'Il piano di studi della matricola: ' + str(matricola) + 'e composto dai seguenti insegnamenti: ' + str(insegnamenti) + '\n'
        return stringa
                    
                    
    def massimoNumeroVolteScelto(self):       
        lista_insegnamenti = []
        for matricola in self._diz:
            for insegnamento in self._diz[matricola]:
                if insegnamento not in lista_insegnamenti:
                    lista_insegnamenti.append(insegnamento)

        massimo = 0

        for insegnamento in lista_insegnamenti:
            count = 0
            for matricola in self._diz:
                if insegnamento in self._diz[matricola]:
                    count += 1
            if count > massimo:
                massimo = count
        return massimo


def main():

    pianodistudi = PianiDiStudi()
    pianodistudi.aggiungiStudente(211356)
    pianodistudi.aggiungiStudente(45698)
    pianodistudi.aggiungiStudente(16496)
    pianodistudi.aggiungiStudente(47856)
    pianodistudi.eliminaStudente(47856)
    pianodistudi.aggiungiInsegnamentoalPiano(211356, "italiano")
    pianodistudi.aggiungiInsegnamentoalPiano(16496, "filosofia")
    pianodistudi.aggiungiInsegnamentoalPiano(211356, "filosofia")
    pianodistudi.aggiungiInsegnamentoalPiano(45698, "filosofia")
    pianodistudi.aggiungiInsegnamentoalPiano(211356, "latino")
    pianodistudi.aggiungiInsegnamentoalPiano(211356, "matematica")
    pianodistudi.aggiungiInsegnamentoalPiano(45698, "storia")
    pianodistudi.aggiungiInsegnamentoalPiano(45698, "latino")
    pianodistudi.aggiungiInsegnamentoalPiano(45698, "educazionefisica")
    pianodistudi.aggiungiInsegnamentoalPiano(16496, "educazionefisica")
    pianodistudi.aggiungiInsegnamentoalPiano(16496, "latino")
    pianodistudi.aggiungiInsegnamentoalPiano(16496, "scienze")
    pianodistudi.eliminaInsegnamentoDalPiano(16496, "educazionefisica")
    print(pianodistudi)
    print(pianodistudi.insegnamentoSceltoDaNessuno("educazionefisica"))
    print(pianodistudi.insegnamentiSceltiDaTutti())
    print(pianodistudi.massimoNumeroVolteScelto())
main()
