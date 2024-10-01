#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lavecchia Nicola 212169

from Impresa_Lavecchia_212169 import Impresa
import pandas as pd

def main():
    file = input('Inserisci il nome del file o premi invio per il file di default (imprese_ordinate.txt): ')
    
    if len(file) < 1:
        file = 'imprese_ordinate.txt'
        
    try:
        infile = open(file, "r")
    except IOError:
        print("Errore: Il file non esiste in questa directory")
        exit()
    
    lista = []

    riga_commento = infile.readline()
    riga_vuota = infile.readline()
    line = infile.readline()
    while line != '':
        riga = line.strip().split(",")
        aziende = Impresa.takeList(riga)
        lista.append(aziende)
        line = infile.readline()
    infile.close()

    print()
    print('A- Le', len(lista), 'imprese hanno in media dipendenti e soci rispettivamente pari a: (%.2f, %.2f)' % Medie(lista))
    print()
    print("B- Tra le", len(lista), "aziende la percentuale di imprese con certificazione o con fatturato compreso tra 10.000 e 50.000 è del %.2f" % percentuali(lista), '%')
    print()
    print(funzione_pandas(lista))
    print()
    print()
    dizionarioAteco(lista)

def Medie(imprese):
    somma_dip = 0
    somma_soci = 0
    for elem in imprese:
        somma_dip += elem.get_nDipendenti()
        somma_soci += elem.get_nSoci()
        
    media_dipendenti = somma_dip / len(imprese)
    media_soci = somma_soci / len(imprese)

    return media_dipendenti, media_soci

def percentuali(imprese):
    n = 0
    for elem in imprese:
        if elem.get_certificazione() == True or (elem.get_fatturato() >= 10000 and elem.get_fatturato() <= 50000):
            n += 1
    percentuale = n / len(imprese)
    percentuale *= 100

    return percentuale

def funzione_pandas(imprese):
    denominazione = []
    lista_data = []
    lista_ragioni = []
    for elem in imprese:
        denominazione.append(elem.get_denominazione())
        lista_data.append(elem.get_dataCostituzione())
        lista_ragioni.append(elem.get_ragioneSociale())
    data_frame = pd.DataFrame(data=denominazione, columns=['Denominazione'])
    data_frame['   '] = ''
    data_frame['Data costituzione'] = lista_data
    data_frame['     '] = ''
    data_frame['Ragione sociale'] = lista_ragioni
    df = data_frame[(data_frame['Data costituzione'] > "01/01/2000") & (data_frame['Ragione sociale'] == 'SocietÃ  di capitali')]
    print("C- Le società di capitali costituite dopo l' 01/01/2000 sono:")
    print()
    return df

def dizionarioAteco(imprese):
    dizionario = {}
    for elem in imprese:
        if elem.get_divAteco() in dizionario:
            dizionario[elem.get_divAteco()] += 1
        else:
            dizionario[elem.get_divAteco()] = 1
    print('D- Per ogni divisione Ateco stampo il numero di imprese associate')
    for elem in dizionario:
        print('   Divisione ATECO', elem, ':', dizionario[elem])

main()
