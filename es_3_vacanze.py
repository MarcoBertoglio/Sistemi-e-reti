#Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
#1, 1, 2, 3, 5, 8, 13 (...)
#Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, 
#entro una soglia specifica impostata dall'utente.


def fibonacci(val):
    if val <= 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fibonacci(val-1) + fibonacci(val-2)

print(fibonacci(20))