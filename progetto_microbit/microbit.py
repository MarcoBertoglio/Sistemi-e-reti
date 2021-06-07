import pygame, queue, threading, time, serial
from pygame.constants import MOUSEBUTTONDOWN
from pygame.version import SDL
pygame.init()

#dichiarazione variabili essenziali per lo svolgimento del programma
run = True
width = 1200
height = 620
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#dichiarazione variabili essenziali per lo svolgimento del programma
width_bullet_right = 875
height_bullet = 480
width_bullet_left = 275
velocita = 15

#dichiarazione variabili per il cownt down
counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
cowntDown_font = pygame.font.Font('Cowboys.otf', 100)

#assegnazione immagine di sfondo e ridimensionamento dell'immagine
backgrownd = pygame.image.load('backgrownd.png')
backgrownd = pygame.transform.scale(backgrownd, (width,height))

#assegnazione immagini del logo e ridimensionamento di esso
logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (260,65))

#assegnazione immagini dei personaggi e ridimensionamento di essi
cowboy_left = pygame.image.load('cowboy1.png.png')
cowboy_left = pygame.transform.scale(cowboy_left,(178,225))
cowboy_right = pygame.image.load('cowboy2.png')
cowboy_right = pygame.transform.scale(cowboy_right,(215,263))
cowboy_left_girato = pygame.image.load('cowboy1_girato.png')
cowboy_left_girato = pygame.transform.scale(cowboy_left_girato,(178,225))
cowboy_right_girato = pygame.image.load('cowboy2_girato.png')
cowboy_right_girato = pygame.transform.scale(cowboy_right_girato,(215,263))

#assegnazione immagine della pistola e ridimensionamento di essa
gun_left = pygame.image.load('gun.png')
gun_left = pygame.transform.scale(gun_left,(97,47))
gun_right = pygame.image.load('gun_girata.png')
gun_right = pygame.transform.scale(gun_right,(97,47))
rip = pygame.image.load('rip.png')

#assegnazione immagine proiettile e ridimensionamento di esso
bullet_right = pygame.image.load('bullet.png')
bullet_right = pygame.transform.scale(bullet_right,(65,50))
bullet_left = pygame.image.load('bullet_left.png')
bullet_left = pygame.transform.scale(bullet_left,(65,50))

#creazione coda del thread    
q = queue.Queue()

#dichiarazione della classe per il comunicamento tra Pygame e Mu Editor
class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):
        #serial config
        port = "COM3"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            q.put(data)
            time.sleep(0.01)

rm = Read_Microbit()
rm.start()
pygame.init()

#if che determina chi vince la partita
if counter <= 0:
    keys = (q.get()).split(",")
    if keys[0] == "True" and keys[1] == "False":
        cnt_a = 1
        cnt_b = 0
    elif keys[0] == "False" and keys[1] == "True":
        cnt_a = 0
        cnt_b = 1

#while true del gioco
while run == True: 
    #eventi necessari per l'apertura della finestra             
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'BANG!'
        
        if e.type == pygame.QUIT: 
            run = False

    #stampa a video dello sfondo
    screen.blit(backgrownd,(0,0))
    screen.blit(logo, (950,0))
    
    #if che determina la posizione dei personaggi in base al cownt down
    if counter == 3:
        screen.blit(cowboy_left,(375,350))
        screen.blit(cowboy_right,(700,350))
    elif counter == 2:
        screen.blit(cowboy_left,(275,350))
        screen.blit(cowboy_right,(800,350))
    elif counter == 1:
        screen.blit(cowboy_left,(175,350))
        screen.blit(cowboy_right,(900,350))
    elif counter <= 0:
        if cnt_a == 1 and cnt_b == 0:
            screen.blit(cowboy_left_girato,(175,350))
            screen.blit(cowboy_right_girato,(900,350))
            screen.blit(bullet_left,(width_bullet_left,height_bullet))
            width_bullet_left += velocita
            screen.blit(gun_left,(275,490))
            if width_bullet_left >= 900:
                screen.blit(rip,(900,350))
                screen.blit(cowboy_right_girato).remove
        elif cnt_a == 0 and cnt_b == 1:
            screen.blit(cowboy_right_girato,(900,350))
            screen.blit(cowboy_left_girato,(175,350))
            screen.blit(bullet_right,(width_bullet_right,height_bullet))
            width_bullet_right -= velocita
            screen.blit(gun_right,(875,490))
            if width_bullet_right <= 175:    
                screen.blit(rip,(175,350))
                screen.blit(cowboy_left_girato).remove

    #stampa a video del cownt down
    cowntDown = cowntDown_font.render(text, True, (0, 0, 0))
    cowntDown_rect = cowntDown.get_rect(center = (600,100))
    screen.blit(cowntDown, cowntDown_rect)
        
    pygame.display.flip()
    clock.tick(60)

#chiusura thread
rm.terminate()
rm.join()