cd "C:\Users\nicol\Desktop\Demografia computazionale\Simulazione\Simulazione 1"
use Integrometro_per_esame

des
summ

rename v01B proprietaLinguaggio
rename v04 linguaggioRivista

*Stato civile
tab v28
tab v28, m nol
rename v28 statoCivile

summ statoCivile

gen celNub = 0
replace celNub=1 if statoCivile==1

gen coniug = 0
replace coniug=1 if statoCivile==2 | statoCivile==99 | statoCivile==.

gen ved = 0
replace ved=1 if statoCivile==3

gen div = 0
replace div=1 if statoCivile==4

global statoCivile "situazione sentimentale"

*Titolo di studio

rename v29 titoloStudio
tab titoloStudio
tab titoloStudio, m nol

gen zeroTituli_obbligo = 0
replace zeroTituli_obbligo=1 if titoloStudio==1 | titoloStudio == 2

gen superiori = 0
replace superiori=1 if titoloStudio==3 | titoloStudio==.

gen uniNo = 0
replace zeroTituli_obbligo=1 if titoloStudio==4 | titoloStudio == 99

global titoloStudio "anno di studio"

*cittadinanza

rename v26 cittadinanza
tab cittadinanza, sort
tab cittadinanza,sort m nol

gen prima = 0
replace prima = 1 if cittadinanza== 436

gen seconda = 0
replace seconda = 1 if cittadinanza== 235

gen terza = 0
replace terza = 1 if cittadinanza== 201

gen quarta = 0
replace quarta = 1 if cittadinanza== 243

gen quinta = 0
replace quinta = 1 if cittadinanza== 314

gen altro = 0
replace altro = 1 if cittadinanza != 436 & cittadinanza != 235 & cittadinanza != 201 & cittadinanza != 243 & cittadinanza != 314


*eta in classi

tab eta
tab eta, m nol
summ eta

gen 18_20 = 0
replace 18_20 = 1 if eta >= 18 & eta <= 20




 

