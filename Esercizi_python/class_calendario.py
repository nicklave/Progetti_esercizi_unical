import copy
class calendario:

    def __init__(self):
        self.diz = {}

    def aggiungiData(self, data):
        if data not in self.diz:
            self.diz[data] = []
            return True
        else:
            return False

    def eliminadata(self, data):
        if data in self.diz:
            self.diz.pop(data)
            return True
        else:
            return False

    def aggiungiImpegno(self, data, impegno):
        if data in self.diz and impegno not in self.diz[data]:
            self.diz[data].append(impegno)
            return True
        else:
            return False

    def eliminaImpegno(self, data, impegno):
        if data in self.diz and impegno in self.diz[data]:
            self.diz[data].remove(impegno)
            return True
        else:
            return False


    def impegnoSemprePresente(self, impegno):
        for data in self.diz:
                if impegno not in self.diz[data]:
                    return False
        return True


    def giornopiuImpegnato(self):
        massimo = 0
        data_max = ''
        for data in self.diz:
            if len(self.diz[data]) > massimo:
                massimo = len(self.diz[data])
                data_max = data
        return data_max

    def __repr__(self):
        stringa = ''
        for (data, impegno) in self.diz.items():
            stringa += 'In data: ' + data + ' ci sono i seguenti impegni: ' + str(impegno) + '\n'
        return stringa


    def lista_impegni(self):
        lista = []
        for data in self.diz:
            for impegno in self.diz[data]:
                if impegno not in lista:
                    lista.append(impegno)
        return lista
    
    # [studio,gioco,corriere]

    def impegnopiuFrequente(self):
        massimo = 0
        impegno_max = ''
        for impegno in self.lista_impegni():
            count = 0
            for data in self.diz:
                if impegno in self.diz[data]:
                    count += 1
            if count > massimo:
                massimo = count
                impegno_max = impegno
        return impegno_max
def main():
    cal = calendario()
    cal.aggiungiData('08/02')
    cal.aggiungiData('10/02')
    cal.aggiungiData('11/02')
    cal.aggiungiImpegno('08/02', 'studio')
    cal.aggiungiImpegno('08/02', 'gioco')
    cal.aggiungiImpegno('10/02', 'studio')
    cal.aggiungiImpegno('10/02', 'corriere')
    cal.aggiungiImpegno('11/02', 'studio')
    cal.aggiungiImpegno('10/02', 'gioco')
    cal.aggiungiImpegno('11/02', 'gioco')
    cal.eliminaImpegno('11/02', 'gioco')
    print(cal)

    print(cal.impegnoSemprePresente('studio'))
    print(cal.giornopiuImpegnato())
    print(cal.impegnopiuFrequente())
main()
    
    









