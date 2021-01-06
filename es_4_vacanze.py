#Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene 
#sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
#Scrivi una semplice funzione in grado di criptare una stringa passata, 
#o decriptarla se la stringa è già stata precedentemente codificata.

def cripta (stringa):
    newStringa = ""
    for k in range (len(stringa)):
        newStringa = newStringa + "".join(chr(ord(stringa[k]) + 15))
    return newStringa

def decripta(stringa):
    newStringa=""
    for k in range(len(stringa)):
        newStringa = newStringa + "".join(chr(ord(stringa[k]) - 15))
    return newStringa

print(cripta("ciao"))
print(decripta("rxp~"))