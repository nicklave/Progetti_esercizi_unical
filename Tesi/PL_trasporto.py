from pulp import *

# Creazione lista magazzini
magazzini = ["A", "B"]

# Creazione di un dizionario che associa ad ogni magazzino la propria disponibilita' di casse
fornitura = {"A": 1000, "B": 4000}

# Crazione lista bar
bar = ["1", "2", "3", "4", "5"]

# Creazione di un dizionario che associa ad ogni bar la quantita' ordinata
ordini = {
    "1": 500,
    "2": 900,
    "3": 1800,
    "4": 200,
    "5": 700,
}

# Creazione di una matrice dei costi
costi = [  # Bar
    # 1 2 3 4 5
    [2, 4, 5, 2, 1],  # A   Magazzini
    [3, 1, 3, 2, 3],  # B
]

# I dati dei costi vengono trasformati in un dizionario associato alle liste di magazzini e bar
costi = makeDict([magazzini, bar], costi, 0)

# Creazione della variabile problema
prob = LpProblem("Problema di trasporto della birra", LpMinimize)

# Creazione di una lista di tuple che contiene ogni possibile associazione di consegna magazzino-bar
consegne = [(m, b) for m in magazzini for b in bar]

# viene creato un dizionario per contenere le variabili decisionali riferite alle consegne
variabili = LpVariable.dicts("Consegna", (magazzini, bar), 0, None, LpInteger)

# Viene aggiunta la funzione obiettivo al problema
prob += (
    lpSum([variabili[m][b] * costi[m][b] for (m, b) in consegne]),
    "Somma totale dei costi di consegna",
)

# Vengono aggiunti al problema i vincoli di fornitura dei magazzini
for m in magazzini:
    prob += (
        lpSum([variabili[m][b] for b in bar]) <= fornitura[m],
        f"Somma dei prodotti inviati dal magazzino_{m}",
    )

# Vengono aggiunti al problema i vincoli di richiesta degli ordini da parte dei bar
for b in bar:
    prob += (
        lpSum([variabili[m][b] for m in magazzini]) >= ordini[b],
        f"Somma dei prodotti ricevuti dal bar{b}",
    )


# Il problema viene risolto utilizzando il risolutore scelto da PuLP
prob.solve()

# Lo stato del problema viene stampato su schermo
print("Status:", LpStatus[prob.status])

# Ogni variabile viene stampata con il suo valore ottimo
for v in prob.variables():
    print(v.name, "=", round(v.varValue))

# Il valore ottimo della funzione obiettivo viene stampato
print("Costo totale del trasporto = ", value(prob.objective))
