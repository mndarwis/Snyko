# File Created: November 4, 2:48 pm
# Maryam Al-Darwish
# Andrew ID : mndarwis
# Snake game ( single and multiplayer modes ) 
from Tkinter import*
import tkMessageBox
from PIL import Image, ImageTk
import pygame
import sys
from pygame.locals import*
import random


#if esc key is pressed : 
def closewindow(event):
    global master
    master.withdraw()


#for the quitbutton in the home page :
def quitgame():
    global wnd
    wnd.withdraw()

#window for 1 player :
#http://pygame.org/docstest/ref/draw.html
#https://www.pinterest.com/pin/352828952040306067/ >> background
def SingleModeGame():
    global wnd
    global Smode
    global Square
    wnd.withdraw()
    pygame.init()
    x = 20
    y = 20
    dx = 0
    dy = 0
    clock = pygame.time.Clock()
    
    
    Smode = pygame.display.set_mode((800,500))
    #Smode.fill((0,191,255))
    pygame.display.set_caption('Single Player')
    background = pygame.image.load("snakebg.png")
    Smode.blit(background, (0,0))
    Square = pygame.draw.rect(Smode, (176,48,96), (x,y,27,27), 0)
    P = pygame.draw.circle(Smode, (30,144,255), (50,100), 15, 0)
    xp = 50
    yp = 100
    gameExit = False
    pygame.time.set_timer(pygame.USEREVENT+1,3000)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                quit()
                #game exits!
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -10
                    
                if event.key == pygame.K_RIGHT:
                    dx = 10

                if event.key == pygame.K_DOWN:
                    dy = 10
            
                if event.key == pygame.K_UP:
                    dy = -10

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                    dx = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    dy = 0
            if event.type == pygame.USEREVENT+1:
                xp,yp = movePoint()
                
#####show "you lose" window#####
                    
        if x > 764 :
            x = 764
            print "Instructions said don't get to the edges!, you lose"
            
        if y > 460 :
            y = 460
            print "Instructions said don't get to the edges!, you lose"
            
        if x < 10 :
            x = 10
            print "Instructions said don't get to the edges!, you lose"
            
        if y <10 :
            y = 10
            print "Instructions said don't get to the edges!, you lose"
        
        x = x + dx
        y = y + dy
        #Smode.fill((0,191,255))
        Smode.blit(background, (0,0))

        moveS(x,y)
      
        xp,yp = points(xp,yp)

        pygame.display.update()
        clock.tick(100)
        

            
        
def moveS(x,y):
    global Smode
    global Square
    Square = pygame.draw.rect(Smode, (176,48,96), (x,y,27,27), 0)


def movePoint():
    global P
    x = random.randint(10,780)
    y = random.randint(20, 460)
    return (x,y)

def points(x,y):
    global P
    P = pygame.draw.circle(Smode, (30,144,255), (x,y), 15, 0)
    return (x,y)
    
    
#shows the instructions to the game .. 
def instructionsWindow():
###http://www.nerdparadise.com/tech/python/pygame/basics/part5/###
    pygame.init()

    Instwnd = pygame.display.set_mode((500,500))
    Instwnd.fill((0,100,130))
    pygame.font.init()
    basicFont = pygame.font.SysFont(None, 30)
    text = basicFont.render("Instructions: Don't get to the edges! ", True, (0,200,0))
    text1 = basicFont.render("enjoy playing :) .. ", True, (0,200,0))
    

    Instwnd.blit(text,(60,40))
    Instwnd.blit(text1,(60,63))


    pygame.display.update()
   

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
      

#multiplayer mode, not done yet :) 
def MultiplayerModeGame():
    print "Not Done Yet"





def Homepage():
    global wnd
    global Instwnd
    
    #image from : http://images.clipartpanda.com/snake-clip-art-snake-hi.png
    snyko = "snyko.png"

    wnd = Tk()
    wnd.geometry("950x650")
    wnd.title("Home Page")

    #wnd.wm_attributes("-fullscreen", True)
    wnd.configure(background = "white")
    img = ImageTk.PhotoImage(Image.open(snyko))

    panel = Label(wnd, image = img)
    panel.grid(row= 0, column=0, columnspan= 30, rowspan= 20)


    #single button
    pic1 = "single.png"
    img1 = ImageTk.PhotoImage(Image.open(pic1))
    SingleMode = Button(wnd, image = img1 , width="130", height="50", command = SingleModeGame)


    #multiplayer button
    pic2 = "multiplayer.png"
    img2 = ImageTk.PhotoImage(Image.open(pic2))
    MultiplayerMode = Button (wnd, image = img2, width="130", height="50", command = MultiplayerModeGame)

    #settings button
    pic3 = "settings.png"
    img3 = ImageTk.PhotoImage(Image.open(pic3))
    Settings = Button (wnd, image = img3, width="130", height="50")

    #instructions button
    pic4 = "instructions.png"
    img4 = ImageTk.PhotoImage(Image.open(pic4))
    Instructions = Button (wnd, image = img4, width="130", height="50", command = instructionsWindow)

    #quit button
    pic5 = "quit.png"
    img5 = ImageTk.PhotoImage(Image.open(pic5))
    Quit = Button (wnd, image = img5, width="130", height="50", command = quitgame)


    SingleMode.grid(row = 5 , column = 15)
    MultiplayerMode.grid(row = 6, column = 15)
    Settings.grid(row = 7 , column = 15)
    Instructions.grid(row = 8, column = 15)
    Quit.grid(row = 9, column = 15)

    wnd.mainloop()


Homepage()
