from microbit import *
while True:
    bottoneA = button_a.is_pressed()
    bottoneB = button_b.is_pressed()
    print(str(bottoneA) + "," + str(bottoneB) + ",")
    sleep(10)
