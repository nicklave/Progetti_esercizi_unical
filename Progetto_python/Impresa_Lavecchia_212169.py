#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lavecchia Nicola 212169

import datetime

class Impresa:
    def __init__(self, cf, partitaIVA, denominazione, ragioneSociale, divAteco, nDipendenti, nSoci, nAmministratori, dataCostituzione, certificazione, fatturato):
        self._cf = cf
        self._partitaIVA = partitaIVA
        self._denominazione = denominazione
        self._ragioneSociale = str(ragioneSociale)
        self._divAteco = divAteco
        self._nDipendenti = int(nDipendenti)
        self._nSoci = int(nSoci)
        self._nAmministratori = int(nAmministratori)        
        self._dataCostituzione = datetime.datetime.strptime(dataCostituzione, '%d/%m/%Y')
        self._certificazione = bool(int(certificazione))  # Impresa.takeBool(certificazione)
        self._fatturato = float(fatturato)

    def get_cf(self):
        return self._cf     
    def get_partitaIVA(self):
        return self._partitaIVA
    def get_denominazione(self):
        return self._denominazione
    def get_ragioneSociale(self):
        return self._ragioneSociale
    def get_divAteco(self):
        return self._divAteco
    def get_nDipendenti(self):
        return self._nDipendenti
    def get_nSoci(self):
        return self._nSoci
    def get_nAmministratori(self):
        return self._nAmministratori
    def get_dataCostituzione(self):
        return self._dataCostituzione
    def get_certificazione(self):
        return self._certificazione
    def get_fatturato(self):
        return self._fatturato
    
    def set_cf(self, cf):
        self._cf = cf
    def set_partitaIVA(self, partitaIVA):
        self._partitaIVA = partitaIVA
    def set_denominazione(self, denominazione):
        self._denominazione = denominazione
    def set_ragioneSociale(self, ragioneSociale):
        self._ragioneSociale = ragioneSociale
    def set_divAteco(self, divAteco):
        self._divAteco = divAteco
    def set_nDipendenti(self, nDipendenti):
        self._nDipendenti = int(nDipendenti)
    def set_nSoci(self, nSoci):
        self._nSoci = int(nSoci)
    def set_nAmministratori(self, nAmministratori):
        self._nAmministratori = int(nAmministratori)
    def set_dataCostituzione(self, dataCostituzione):
        self._dataCostituzione = datetime.datetime.strptime(dataCostituzione, '%d/%m/%Y')
    def set_certificazione(self, certificazione):
        self._certificazione = bool(int(certificazione))
    def set_fatturato(self, fatturato):
        self._fatturato = float(fatturato)
        

    def __str__(self):
        stampa = ('\nImpresa \nCodice Fiscale: ' + self._cf + '\nPartita IVA: ' + self._partitaIVA + '\nDenominazione: ' + self._denominazione
                  + '\nRagione Sociale: ' + self._ragioneSociale + '\nDivisione ATECO: ' + self._divAteco + '\nNumero dipendenti: ' + str(self._nDipendenti)
                  + '\nNumero soci: ' + str(self._nSoci) + '\nNumero amministratori: ' + str(self._nAmministratori)
                  + '\nData Costituzione: ' + str(self._dataCostituzione) + '\nCertificazione di qualità: ' + str(self._certificazione)
                  + '\nFatturato: ' + str(self._fatturato))
        return stampa

    @classmethod
    def takeList(cls, lista):
        return cls(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10])
    
    # @staticmethod
    # def takeBool(certificazione):
        # if certificazione == 'True':
            # return True
        # elif certificazione == 'False':
            # return False

    def __lt__(self, other):
        if self._divAteco < other._divAteco:
            return True
        if self._divAteco == other._divAteco and self._nAmministratori > other._nAmministratori:
            return True
        else:
            return False
        
    def dirittoAgevolazione(self):
        if self._divAteco == 'A03' and self._nDipendenti > 15:
            return True
        else:
            return False
    
    def calcolaImposta(self):
        coefficiente = 0
        aliquota = 0
        if self._fatturato >= 10000 and self._fatturato <= 50000:
            coefficiente = 1.2
            aliquota = 0.0049
        if self._fatturato > 50000 and self._fatturato <= 150000:
            coefficiente = 1.5
            aliquota = 0.0076
        if self._fatturato > 150000:
            coefficiente = 1.7
            aliquota = 0.0081
            
        IRAP = self._fatturato * coefficiente * aliquota

        if self.dirittoAgevolazione():
            riduzione = IRAP * 0.015
            IRAP -= riduzione
            
        return IRAP

        
        

        
        



