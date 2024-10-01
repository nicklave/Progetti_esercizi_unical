cd "C:\Users\nicol\Desktop\Demografia computazionale\simulazionidemografia\15_06_2017 e 22_09_2017"

use Integrometro_per_esame.dta

d
s

rename v09B piacere_lavorare

rename v28 statoCivile
tab statoCivile
tab statoCivile, m nol
gen celnub = 0
replace celnub = 1 if statoCivile == 1
gen coniug = 0
replace coniug = 1 if statoCivile == 2 | statoCivile == 99 | statoCivile == .
gen vedovo = 0
replace vedovo = 1 if statoCivile == 3
gen divorz = 0
replace divorz = 1 if statoCivile == 4
global statoCivile "celnub coniug vedovo"

rename v29 titoloStudio
tab titoloStudio
tab titoloStudio, m nol
gen nessuno = 0
replace nessuno = 1 if titoloStudio == 1
gen scuolaObbligo = 0
replace scuolaObbligo = 1 if titoloStudio == 2
gen scuolaSup = 0
replace scuolaSup = 1 if titoloStudio == 3 | titoloStudio == 99 | titoloStudio ==.
gen laurea = 0
replace laurea = 1 if titoloStudio == 4

rename v30 religione
tab religione
tab religione, m nol
gen musulmana = 0
replace musulmana = 1 if religione == 1
gen cristiana = 0
replace cristiana = 1 if  religione == 2 | religione == 3 | religione == 6
gen altraRel = 0
replace altraRel = 1 if  religione != 2 & religione != 3 & religione != 6 & religione != 1
global religione "musulmana cristiana"

rename v32 nazionalitaConiuge
tab nazionalitaConiuge
tab nazionalitaConiuge, m nol
gen coniugeIta = 0
replace coniugeIta = 1 if nazionalitaConiuge == 1

rename v26 cittadinanza
tab cittadinanza, sort
tab cittadinanza, sort m nol
gen marocco = 0
replace marocco = 1 if cittadinanza == 436
gen romania = 0
replace romania = 1 if cittadinanza == 235
gen albania = 0
replace albania = 1 if cittadinanza == 201
gen ucraina = 0
replace ucraina = 1 if cittadinanza == 243
gen cina = 0
replace cina = 1 if cittadinanza == 314
gen altre = 0
replace altre = 1 if cittadinanza != 436 & cittadinanza != 235 & cittadinanza != 201 & cittadinanza != 243 & cittadinanza != 314
global cittadinanza "marocco albania ucraina cina altre"

rename v14 rimanere_italia
tab rimanere_italia
tab rimanere_italia, m nol
gen perSempre = 0
replace perSempre = 1 if rimanere_italia == 1

tab eta
tab eta, nol m
gen da18_a19=0
replace da18_a19=1 if eta==18 | eta==19
gen da20_a24=0
replace da20_a24=1 if eta>19 & eta <25
gen da25_a29=0
replace da25_a29=1 if eta>24 & eta <30
gen da30_a34=0
replace da30_a34=1 if eta>29 & eta <35
gen da35_a39=0
replace da35_a39=1 if eta>34 & eta <40
gen da40_a44=0
replace da40_a44=1 if eta>39 & eta <45
gen da45_a49=0
replace da45_a49=1 if eta>44 & eta <50
gen piu50=0
replace piu50=1 if eta>49
global classi_eta "da18_a19 da20_a24 da25_a29 da30_a34 da35_a39 da40_a44 da45_a49"

summ eta, detail
summ cittadinanza, detail
summ religione, detail

rename v23 genere
tab genere
tab genere, m nol
gen uomo = 0
replace uomo = 1 if genere = 1

tab religione v05
tab cittadinanza v05

