import pygame
import time
from random import randint

pygame.init()

clock = pygame.time.Clock()
clock.tick(40)
back = (0, 255, 255) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
#цвета
LIGHT_BLUE = (200, 200, 255)

class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height) #прямоугольник
       self.fill_color = color


   def color(self, new_color):
       self.fill_color = new_color
 
   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)

   def outline(self, frame_color, thickness):
       pygame.draw.rect(mw, frame_color, self.rect, thickness)

   def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)   

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('veranda',fsize).render(text,True,text_color)
  
    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        mw.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))

YELLOW = (255,255,0)
DARK_BLUE = (0,0,100)
BLUE = (80, 80, 255)
GREEN = (76,153,0)
LIGHT_GREEN = (0,255,0)
RED = (250,0,0)
DARK_RED = (153,0,0)
YA_BIBA = (153,255,255)
cards = []
num_cards = 4

x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x += 100

wait = 0


start_time = time.time()
cur_time = start_time

points = 0

time_text = Label(0,0,30,50,back)
time_text.set_text('Время:',40, DARK_BLUE)
time_text.draw(20, 20)
 

timer = Label(50,50,50,30,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)

score_text = Label(370,0,50,50,back)
score_text.set_text('Счёт:',45, DARK_BLUE)
score_text.draw(20,20)
 
score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)


while True:
    if wait == 0:
        #переносим надпись:
        wait = 20 #столько тиков надпись будет на одном месте
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i+1 == click: 
                        print('попал!')
                        cards[i].color(GREEN)
                        points += 1
                    else: 
                        print('мимо!')
                        cards[i].color(RED)
                        points -= 1
 
                    cards[i].fill()
                    score.set_text(str(points),40, DARK_BLUE)
                    score.draw(0,0)
    new_time = time.time()

    if new_time - start_time >= 11:
        win = Label(0,0,500,500,DARK_RED)
        win.set_text('Время вышло', 60, YA_BIBA)
        win.draw(110,180)
        break

    if int(new_time) - int(cur_time) == 1:
        timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer.draw(0,0)
        cur_time = new_time
 
    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("YOU WIN!!", 60, DARK_BLUE)
        win.draw(140, 180)
        resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        resul_time.set_text("Время прохождения: " + str (int(new_time - start_time)) + " сек", 40, DARK_BLUE)
        resul_time.draw(0, 0)
 
        break

    pygame.display.update()
    clock.tick(40)
pygame.display.update()
