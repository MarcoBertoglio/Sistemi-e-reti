#Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 
# ad oggi, proveniente da varie fonti (colonna “Source”). Scrivere un programma che generi un dizionario 
# che abbia come chiave l’anno (“Year”) e valore la media aritmetica delle anomalie registrate dalle varie 
# fonti durante quell’anno.
#Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la 
#anomalia massima e minima nel periodo compreso tra anno_1 e anno_2.

import csv

annoPrec = 0
dizionario = {0: 0}

with open("annual.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=",")
    for k in lettore:
        k[2] = float(k[2])
        if k[1] == annoPrec:
            dizionario[annoPrec] = (dizionario[annoPrec] + k[2]) / 2
        else:
            dizionario[k[1]] = k[2]
            annoPrec = k[1]


def anomaliaMax(anno1, anno2):
    max = dizionario[anno1]
    for k in range (int (anno1), int (anno2)+1, 1):
        if max < dizionario[str(k)]:
            max = dizionario[str(k)]
    print(max)


anomaliaMax("2000", "2016")

