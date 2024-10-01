"""
Tesi di laurea triennale Nicola Lavecchia
Problema di programmazione lineare in Python
Esempio Cibo per gatti Whiskas tramite il modellatore PuLP
"""

from pulp import *

problema = LpProblem("Problema", LpMinimize)


x1 = LpVariable("Percentuale Pollo", 0, None, LpInteger)
x2 = LpVariable("Percentuale Manzo", 0, None, LpInteger)
x3 = LpVariable("Percentuale Montone", 0, None, LpInteger)
x4 = LpVariable("Percentuale Riso", 0, None, LpInteger)
x5 = LpVariable("Percentuale Grano", 0, None, LpInteger)
x6 = LpVariable("Percentuale Gel", 0, None, LpInteger)

problema += 0.013 * x1 + 0.008 * x2 + 0.010 * x3 + 0.002 * x4 + 0.005 * x5 + 0.001 * x6, "Costo totale ingredienti per porzione"

problema += x1 + x2 + x3 + x4 + x5 + x6 == 100, "Percentuale somma a 100"
problema += 0.100 * x1 + 0.200 * x2 + 0.150 * x3 + 0.000 * x4 + 0.040 * x5 + 0.000 * x6 >= 8.0, "Richiesta proteine"
problema += 0.080 * x1 + 0.100 * x2 + 0.110 * x3 + 0.010 * x4 + 0.010 * x5 + 0.000 * x6 >= 6.0, "Richiesta Grasso"
problema += 0.001 * x1 + 0.005 * x2 + 0.003 * x3 + 0.100 * x4 + 0.150 * x5 + 0.000 * x6 <= 2.0, "Richiesta fibre"
problema += 0.002 * x1 + 0.005 * x2 + 0.007 * x3 + 0.002 * x4 + 0.008 * x5 + 0.000 * x6 <= 0.4, "Richiesta sale"

problema.solve()

print("Stato del problema: ", LpStatus[problema.status])
print()

for variabile in problema.variables():
    print(variabile.name, " = ", variabile.varValue)

print()

print("Costo totale degli ingredienti per porzione: ", value(problema.objective))
