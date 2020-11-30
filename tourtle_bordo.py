import turtle

robot = turtle.Turtle()
bordo = turtle.Turtle()
schermo = turtle.Screen()
bordo.goto(0,0)
robot.penup()
bordo.speed(10)

def disegnaBordo():
    bordo.penup()
    bordo.goto(-200,-200)
    bordo.pendown()

    for k in range (4):
        bordo.forward(400)
        bordo.left(90)

def sinistra():
    robot.left(90)

def destra():
    robot.right(90)

def jump():
    coordinate = robot.position()
    print(coordinate)

    if(coordinate[0] < 175 and coordinate[0] > -175 and coordinate[1] < 175 and coordinate[1] > -175):
        robot.forward(25)
    else:
        robot.goto(0,0)


disegnaBordo()
schermo.title("My game")
schermo.bgcolor("green")
schermo.setup(width = 800, height = 800)

schermo.listen()                        #mette la finestra in ascolto di eventi (es: pressione tasti)
schermo.onkey(sinistra, "Left")
schermo.onkey(destra, "Right")
schermo.onkey(jump, "space")


schermo.title("My game")
schermo.bgcolor("green")
schermo.setup(width=800, height=800)

schermo.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
schermo.onkey(jump, "space")
schermo.onkey(sinistra, "Left")
schermo.onkey(destra, "Right")

schermo.mainloop()