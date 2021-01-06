#Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, 
#composto da 6 coppie di cifre esadecimali separate da due punti.
#Un esempio di MAC è 02:FF:A5:F2:55:12.
#Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

import random

supporto = ['0','1','2','3','4','5','6','7','8','9','a','b','c', 'd','e','f']

def generaMac(val):
    mac = ""
    for k in range (val):
        mac = mac + supporto[random.randint(0,len(supporto)-1)]
        mac = mac + supporto[random.randint(0,len(supporto)-1)]
        mac = mac +":"

    return mac

def main():
    val = 6
    mac = generaMac(val)
    print(mac)

if __name__=="__main__":
    main()
