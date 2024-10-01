#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lavecchia Nicola 212169

from Impresa_Lavecchia_212169 import Impresa

def main():
    file = input('Inserisci il nome del file o premi invio per il file di default (imprese.txt): ')
    if len(file) < 1:
        file = 'imprese.txt'
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
    
    lista.sort()
    print(visualizza_dati(lista))
    save_in_file(lista)
    
def dizionario(imprese):
    somma = 0
    diz = {}
    for elem in imprese:
        somma = elem.get_nDipendenti() + elem.get_nSoci() + elem.get_nAmministratori()
        diz[elem.get_cf()] = somma

    return diz

def visualizza_dati(imprese):
    for elem in imprese:
        print(elem)
        irap = elem.calcolaImposta()
        print("L'importo totale IRAP da pagare è: € %.2f" % irap)
    print()
    print("Per ogni codice fiscale stampo il totale delle persone coinvolte nell'impresa:")

    diz = dizionario(imprese)

    for elem in diz:
        print(elem, ':', diz[elem])



def save_in_file(imprese):
    outfile = open("imprese_ordinate.txt", "w")
    outfile.write('# Riguardo il penultimo elemento(certificazione di qualità) 0=False 1=True \n')
    outfile.write('\n')
    for elem in imprese:
        formatta_data = elem.get_dataCostituzione().strftime("%d/%m/%Y")
        if elem.get_certificazione() == True:
            booleana = 1
        elif elem.get_certificazione() == False:
            booleana = 0
        stringa_per_file = elem.get_cf() + ',' + elem.get_partitaIVA() + ',' + elem.get_denominazione() + ',' + elem.get_ragioneSociale() + ',' + elem.get_divAteco() + ',' + str(elem.get_nDipendenti()) + ',' + str(elem.get_nSoci()) + ',' + str(elem.get_nAmministratori()) + ',' + str(formatta_data) + ',' + str(booleana) + ',' + str(elem.get_fatturato()) + '\n'
        outfile.write(stringa_per_file)
    outfile.close()
    
main()


