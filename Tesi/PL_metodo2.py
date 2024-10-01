"""
Tesi di laurea triennale Nicola Lavecchia
Problema di programmazione lineare in Python
Esempio Cibo per gatti Whiskas tramite il modellatore PuLP
"""

from pulp import *

# Si importano i costi e la tabella in Python tramite l'uso dei dizionari

# Lista degli ingredienti

ingredienti = ["Pollo", "Manzo", "Montone", "Riso", "Grano", "Gel"]

# Dizionario dei costi di ogni ingrediente

costi = {
    "Pollo": 0.013,
    "Manzo": 0.008,
    "Montone": 0.010,
    "Riso": 0.002,
    "Grano": 0.005,
    "Gel": 0.001}

# Dizionario della percentuale di proteine in ogni ingrediente

proteine = {
    "Pollo": 0.100,
    "Manzo": 0.200,
    "Montone": 0.150,
    "Riso": 0.000,
    "Grano": 0.040,
    "Gel": 0.000}

# Dizionario della percentuale di Grasso in ogni ingrediente

grasso = {
    "Pollo": 0.080,
    "Manzo": 0.100,
    "Montone": 0.110,
    "Riso": 0.010,
    "Grano": 0.010,
    "Gel": 0.000}

# Dizionario della percentuale di fibre in ogni ingrediente

fibre = {
    "Pollo": 0.001,
    "Manzo": 0.005,
    "Montone": 0.003,
    "Riso": 0.100,
    "Grano": 0.150,
    "Gel": 0.000}

# Dizionario della percentuale di sale in ogni ingrediente

sale = {
    "Pollo": 0.002,
    "Manzo": 0.005,
    "Montone": 0.007,
    "Riso": 0.002,
    "Grano": 0.008,
    "Gel": 0.000}


# Creazione della variabile problema
problema = LpProblem("Cibo per gatti Whiskas", LpMinimize)

# Si creano le variabili ingredienti con limite inferiore pari a 0 partendo dalla lista inizialmente creata
# il tutto si converte in dizionario tramite la funzione LpVariable.dicts
variabili_ingredienti = LpVariable.dicts("Ingredienti", ingredienti, 0)


# Si aggiunge al problema la funzione obiettivo tramite l'associazione dei dizionari "costi" e "variabili_ingredienti":

problema += (
    lpSum([costi[i] * variabili_ingredienti[i] for i in ingredienti]),
    "Costo totale degli ingredienti per barattolo",
)

# Si definiscono i vincoli tramite l'associazione del dizionario "variabili_ingredienti" con i dizionari dei singoli ingredienti

problema += (lpSum([variabili_ingredienti[i] for i in ingredienti]) == 100, "Vincolo somma percentuale")

problema += (lpSum([proteine[i] * variabili_ingredienti[i] for i in ingredienti]) >= 8.0, "Requisiti proteine")

problema += (lpSum([grasso[i] * variabili_ingredienti[i] for i in ingredienti]) >= 6.0, "Requisiti grasso")

problema += (lpSum([fibre[i] * variabili_ingredienti[i] for i in ingredienti]) <= 2.0, "Requisiti fibre")

problema += (lpSum([sale[i] * variabili_ingredienti[i] for i in ingredienti]) <= 0.4, "Requisiti sale")

# I dati del problema vengono scritti in un file .lp
problema.writeLP("Modello_Whiskas.lp")

# Si risolve il problema tramite il risolutore scelto da PuLP
problema.solve()

# Si stampa lo stato del problema
print("Status:", LpStatus[problema.status])

# Ogni variabile viene stampata con il suo valore ottimo
for v in problema.variables():
    print(v.name, " = ", round(v.varValue),"%")

# Viene stampato il valore ottimo della funzione obiettivo
print("Costo totale degli ingredienti per barattolo  = ", value(problema.objective), "Euro")