cd"C:\Users\nicol\Desktop\Demografia computazionale\simulazionidemografia\14_07_2017"

use Matrice_Anziani.dta

tab Sesso
tab Sesso,m nol
encode Sesso, generate(sesso)
tab sesso 
tab sesso, m nol

recode sesso (1=99) (2=1) (3=2)
tab sesso, m nol
gen femmina = 0
replace femmina = 1 if sesso == 1

tab stato_civile
tab stato_civile, m nol
encode stato_civile, generate(StatoCivile)
tab StatoCivile, m nol
gen coniugato = 0
replace coniugato = 1 if StatoCivile == 2
gen divorziato = 0
replace divorziato = 1 if StatoCivile == 3
gen nubcel = 0
replace nubcel = 1 if StatoCivile == 4
gen separato = 0
replace separato = 1 if StatoCivile == 5
gen vedovo = 0
replace vedovo = 1 if StatoCivile == 6
global statoCivile "coniugato divorziato nubcel separato"

tab Provincia
tab Provincia, m nol
encode Provincia, generate(provincia)
gen cz = 0
replace cz = 1 if provincia == 1
gen cs = 0
replace cs = 1 if provincia == 2
gen kr = 0
replace kr = 1 if provincia == 3
gen rc = 0
replace rc = 1 if provincia == 4
gen vv = 0
replace vv = 1 if provincia == 5
global province "cz cs rc vv"


tab titolo_studio
tab titolo_studio, m nol
encode titolo_studio, generate(titoloDiStudio)
gen avviamento = 0
replace avviamento = 1 if titoloDiStudio == 2
gen diploma = 0
replace diploma = 1 if titoloDiStudio == 3
gen laurea = 0
replace laurea = 1 if titoloDiStudio == 4
gen licenmedia = 0
replace licenmedia = 1 if titoloDiStudio == 5
gen nessuno = 0
replace nessuno = 1 if titoloDiStudio == 6
gen postlaurea = 0
replace postlaurea = 1 if titoloDiStudio == 7
global titoliStudio "avviamento diploma laurea licenmedia postlaurea"

tab Ore_tv
tab Ore_tv, m nol
encode Ore_tv, generate(oreTv)
gen guarda_tv = 0
replace guarda_tv = 1 if oreTv == 3

tab Difficolta_vita_quotidiana_Nessu
encode Difficolta_vita_quotidiana_Nessu, generate(difficolta)
tab difficolta, m nol
gen haDifficolta  = 0
replace haDifficolta = 1 if difficolta == 1 | difficolta == 3

tab Si_prende_cura_partner
gen cura_partner = 0
replace cura_partner = 1 if Si_prende_cura_partner == "Quotidianamente"

tab Si_prende_cura_figli
gen cura_figli = 0
replace cura_figli = 1 if Si_prende_cura_figli == "Quotidianamente"

tab Si_prende_cura_nipote
gen cura_nipoti = 0
replace cura_nipoti = 1 if Si_prende_cura_nipote == "Quotidianamente"

tab reddito_classi
encode reddito_classi, generate(reddito)
gen reddito_basso = 0
replace reddito_basso = 1 if reddito == 1 | reddito == 3 | reddito == 5
gen reddito_medio = 0
replace reddito_medio = 1 if reddito == 4
gen reddito_alto = 0
replace reddito_medio = 1 if reddito == 2
global Reddito "reddito_basso reddito_medio"

tab Figli_femmine
tab Figli_femmine, m nol
gen haFiglie = 0
replace haFiglie = 1 if Figli_femmine > 0

tab Figli_maschi

gen avere_figli = 0 
replace avere_figli = 1 if Figli_femmine > 0 | Figli_maschi > 0

tab2 avere_figli guarda_tv
tab avere_figli guarda_tv

graph pie, over(haDifficolta) by(reddito_classi)

logit guarda_tv cura_figli $statoCivile avere_figli $Reddito $province $titoliStudio, r or
