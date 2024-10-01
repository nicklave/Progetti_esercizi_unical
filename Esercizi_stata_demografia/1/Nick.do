*modello 
*logit: variabile dipendente binaria
*mlogit: variabile dipendente categoriale
*ologit: variabile dipendente categoriale ordinata(molto  		    soddisfatta, poco soddisfatta ecc..)
*reg: variabile dipendente continua


cd "C:\Users\nicol\Desktop\Demografia computazionale\Simulazione\Simulazione 1"

use Integrometro_per_esame

summarize
describe

rename v07 associazionismo
rename v33B residenza_figli

*stato civile
rename v28 stato_civile
tab stato_civile
tab stato_civile, m nol

gen celNub = 0
replace celNub = 1 if stato_civile ==1

gen coniugato = 0
replace coniugato = 1 if stato_civile ==2 | stato_civile ==99 | stato_civile==.

gen vedovo = 0
replace vedovo = 1 if stato_civile ==3

gen divorzio = 0
replace divorzio = 1 if stato_civile == 4

global stato_civile "celNub coniugato vedovo divorzio"

*titolo di studio
rename v29 titolo_studio
tab titolo_studio
tab titolo_studio, m nol

gen not_obbligo = 0
replace not_obbligo = 1 if titolo_studio ==1 | titolo_studio ==2

gen sup_uni = 0
replace sup_uni = 1 if titolo_studio ==3 | titolo_studio ==4 |  titolo_studio ==99 | titolo_studio ==.

global titolo_studio "not_obbligo sup_uni"

*religione
rename v30 religione
tab religione
tab religione, m nol

gen musulmana = 0
replace musulmana = 1 if religione ==1

gen cristiana = 0
replace cristiana = 1 if religione == 2 | religione == 3 | religione == 6

gen altre = 0
replace altre = 1 if religione != 1 & religione != 2 & religione != 3 & religione != 6

global religione "musulmana cristiana altre"

* nazionalità coniuge 

rename v32 nazionalità_coniuge
tab nazionalità_coniuge
tab nazionalità_coniuge, m nol

gen italiana  = 0
replace italiana = 1 if nazionalità_coniuge == 1

gen europea = 0
replace europea = 1 if nazionalità_coniuge == 2 | nazionalità_coniuge == 99 | nazionalità_coniuge ==.

gen straniera =  0
replace straniera  = 1 if nazionalità_coniuge == 3

global nazionalità_coniuge "italiana europa straniera"

*cittadinanza

rename v26 cittadinanza
tab cittadinanza, sort
tab cittadinanza,sort m nol

gen marocco = 0
replace marocco =1 if cittadinanza == 436

gen romania  = 0
replace romania = 1 if cittadinanza == 235

gen albania  = 0
replace albania = 1 if cittadinanza == 201

gen ucraina  = 0
replace ucraina = 1 if cittadinanza == 243

gen cina  = 0
replace cina = 1 if cittadinanza == 314

gen altre_nazioni = 0
replace altre_nazioni = 1 if cittadinanza != 436 & cittadinanza != 235 & cittadinanza != 201 & cittadinanza != 243 & cittadinanza != 314

global cittadinanza "marocco romania albania ucraina cina altre"

*rimanere in italiana
rename v14 intenzione_restare
tab intenzione_restare
tab intenzione_restare, m nol

gen per_sempre = 0
replace per_sempre = 1 if intenzione_restare ==1

gen non_per_sempre = 0
replace non_per_sempre = 1 if intenzione_restare != 1

globa intenzione_restare "per_sempre non_per_sempre"

* classi eta
tab eta
tab eta, m nol

gen da18a19=0
replace da18a19=1 if eta>=18 & eta<=19
gen da20a24=0
replace da20a24=1 if eta>=20 & eta<=24
gen da25a29=0
replace da25a29=1 if eta>=25 & eta<=29
gen da30a34=0
replace da30a34=1 if eta>=30 & eta<=34
gen da35a39=0
replace da35a39=1 if eta>=35 & eta<=39 | eta==.
gen da40a44=0
replace da40a44=1 if eta>=40 & eta<=44
gen da45a49=0
replace da45a49=1 if eta>=45 & eta<=49
gen da50apiu=0
replace da50apiu=1 if eta>=50 & eta<=90
global eta "da18a19 da20a24 da25a29 da30a34 da35a39 da40a44 da45a49"

summ eta,detail
summ intenzione_restare,detail
summ religione,detail

tab2 religione nazionalità_coniuge

tab2 cittadinanza intenzione_restare

graph pie, over(v11) by(,title (Appartenenza all'Italia rispetto alla religione di appartenenza)) by(religione)

mlogit italiana eta $stato_civile $religione cittadinanza 


