#Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora 
#l'utente voglia una password semplice, 
#o di 20 caratteri ascii qualora desideri una password più complicata.

import random

supporto = ['0','1','2','3','4','5','6','7','8','9','a','b','c', 'd','e','f','g','h','i','j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y','z']

def generaPassword(val):
    password = ""
    for k in range (val):
        password = password + supporto[random.randint(0,len(supporto)-1)]
    return password

def main():
    val = int (input("inserisci la dimensione della password: "))
    password = generaPassword(val)
    print(password)

if __name__=="__main__":
    main()