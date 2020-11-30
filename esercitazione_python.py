import turtle         #importa il modulo turtle
#from turtle import *  importa tutte le classi presenti nel modulo turtle
bob = turtle.Turtle()
bob.color("red")
bob.begin_fill()
nLati = (int) (input("Numero di lati..."))
while True:
    bob.forward(50)
    bob.left(360 / nLati)
    if abs(bob.pos()) <1:
        break
bob.end_fill()