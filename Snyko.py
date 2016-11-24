# File Created: November 4, 2:48 pm
# Maryam Al-Darwish
# Andrew ID : mndarwis
# Snake game - SNYKO - ( single and multiplayer modes, with other "cool" features )
##:) :

from Tkinter import*
import tkMessageBox
from PIL import Image, ImageTk
import pygame
import sys
from pygame.locals import*
import random


bgphoto = "grid.png"

###home page###
def mainwindow():
    global main
    pygame.init()
    main = pygame.display.set_mode((900,600))
    pygame.display.set_caption("SNYKO")
    Background = pygame.image.load("snyko.png")
    main.blit(Background, (0,0))
##font types and sizes:
    basicFont = pygame.font.SysFont(None, 40)
    font = pygame.font.SysFont(None, 44)
##text on screen:
    start = basicFont.render("Press 'S' for single mode", True, (255,255,255))
    main.blit(start, (350,100))
    start = basicFont.render("Press 'M' for multiplayer mode", True, (255,255,255))
    main.blit(start, (350,150))
    start = basicFont.render("Press 'I' for Instructions", True, (255,255,255))
    main.blit(start, (350,200))
    start = basicFont.render("Press 'B' to choose your background", True, (255,255,255))
    main.blit(start, (350,250))
    start = basicFont.render("Press 'Q' to quit", True, (255,255,255))
    main.blit(start, (350,300))
##http://stackoverflow.com/questions/7746263/how-play-mp3-with-pygame##
###add music###
    Musicplay = 'snyko.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(Musicplay)
    a = pygame.mixer.music.get_volume()
    pygame.mixer.music.play()
    pygame.display.update()
###loop to run the window###
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
###inputs from the player(keyboard)###
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    SingleModeGame()
                if event.key == pygame.K_m :
                    MultiplayerMode()
                if event.key == pygame.K_i:
                    instructionswnd()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()
###setting the volume by the player###
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
                if event.key == pygame.K_b:
                    choosebackground()
        main.fill((0,0,0))

    

###single mode window game###
def SingleModeGame():
    global pause
    global Smode
    global Square
    global score
    global bgphoto
    global snake
    global x,y
    global direction
    

    pygame.init()
    score = 0
    equal = False
    subtract = False
    scoretxt = pygame.font.SysFont("monospace", 30)

###x,y are the coordinates for the snake###
    snake = [(25,20),(50,20),(75,20),(100,20)]
    x = 100
    y = 20

###xp,yp for the apple(blue circles)###
###nx, ny for the red circles (the player is not supposed to eat them###
###yx, yy are the yellow circles, they subtract 1 from the player's points###
    xp = 50
    yp = 100
    nx = 200
    ny = 400
    yx = 150
    yy = 230
    clock = pygame.time.Clock()
    direction = 0
    Smode = pygame.display.set_mode((800,500))
###window's title###
    pygame.display.set_caption('Single Player')
###bgphoto can be changed by the player(press b and choose any background)####
    background = pygame.image.load(bgphoto)
    Smode.blit(background, (0,0))
    Square = pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0)
    P = pygame.draw.circle(Smode, (30,144,255), (50,100), 15, 0)
    gameExit = False
###change the position of the cherries every 4 seconds(timer)###
    pygame.time.set_timer(pygame.USEREVENT+1,4000)
###loop###
    while not gameExit:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
                #game exits!
            if event.type == pygame.KEYDOWN:
            ##change the direction of the snake##
                if event.key == pygame.K_LEFT and direction!= 1:
                    direction = 3
                if event.key == pygame.K_RIGHT and direction!= 3:
                    direction = 1 
                if event.key == pygame.K_DOWN and direction!=2:
                    direction = 0
                if event.key == pygame.K_UP and direction!=0:
                    direction = 2
            ##press p to pause the game(call paused function##
                if event.key == pygame.K_p:
                    pause = True
                    paused()
###quit the game and go to the home page###
                if event.key == pygame.K_SPACE:
                    mainwindow()
##########volume settings############
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
##call the functions to get new (x,y) for the cherries (blue, yellow, red)###
            if event.type == pygame.USEREVENT+1:
                xp,yp = movePoint()
                nx, ny = losePoint()
                yx, yy = yellowpoints()
####change directions of the snake####
        if direction == 0:
            y = y + 28
        elif direction == 1:
            x = x + 28
        elif direction == 2:
            y = y - 28
        elif direction == 3:
            x = x - 28

        snake.append((x,y))
        snake = snake[1:]

        Smode.blit(background, (0,0))
    ###moves the snake from the previous x and y###
        moveS(x,y,snake)
    ###moves the cherries from the given x and y###
        xp,yp = points(xp,yp)
        nx, ny = loss(nx , ny)
        yx, yy = moveyellow(yx, yy)

#####update score####
        pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
        Smode.blit(pscore, (20,20))

##if the player scored 20 or more, he will be asked if he wants to continue playing
    #continuegame function will be called to ask the player to continue playing or no
        if score >= 20 :

            continuegame()
        
###if they are close, call the function (change the apple's position)###
        if (abs(x - xp))< 22 and (abs(y-yp))< 22  :
            equal = True
            xp,yp = movePoint()
            score = score + 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
###for the red berries###, the player will lose immediately
        if (abs(x-nx))<22 and (abs(y-ny))<22 :
            youlosewnd()
###for the rotten berries, subtract 1 point###
        if (abs(x - yx))< 22 and (abs(y-yy))< 22  :
            subtract = True
            yx,yy = yellowpoints()
            score = score - 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
##if the score is less than 0 , then set it to zero and show the score on the lose window
            if score < 0 :
                score = 0
                youlosewnd()

###edit length####
        if equal == True :
            snake.append(pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0))
            equal = False
            
        if subtract == True :
            snake = snake[1:]
            subtract = False

        
        
#####show "you lose" window, if the snake hits the walls#####
        if x > 777 :
            youlosewnd()
        if y > 490 :
            youlosewnd()
        if x < 1 :
            youlosewnd()
        if y < -5:
            youlosewnd()
        pygame.display.update()

###do you want to continue playing ?    
def continuegame():
    pygame.init()
    ####text on window####
    cont = pygame.display.set_mode((900,600))
    pygame.display.set_caption("YOU WON")
    Background = pygame.image.load("snyko.png")
    cont.blit(Background, (0,0))
    basicFont = pygame.font.SysFont(None, 40)
    font = pygame.font.SysFont(None, 44)
    start = basicFont.render("YOU WON", True, (255,255,255))
    main.blit(start, (350,100))
    start = basicFont.render("Do you want to continue playing?", True, (255,255,255))
    main.blit(start, (350,150))
    start = basicFont.render("Press 'y' to continue (Hard Mode) ", True, (255,255,255))
    main.blit(start, (350,200))
    start = basicFont.render("Press 'N' to go to main menu ", True, (255,255,255))
    main.blit(start, (350,250))
    start = basicFont.render("Press 'Q' to quit", True, (255,255,255))
    main.blit(start, (350,300))
    
    pygame.display.update()
###loop to run the window###
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
###inputs from the player(keyboard)###
            if event.type == pygame.KEYDOWN:
            ##continue playing
                if event.key == pygame.K_y:
                    hardmode()
            ##go back to the main window
                if event.key == pygame.K_n :
                    mainwindow()

            ##quit game
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()
            ##set the volume
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
    
        main.fill((0,0,0))
    
#####hard single mode, this will start if the player scored 20 or more #####
def hardmode():
    ###get those from the single mode, same direction and same score and size
    global pause
    global Smode
    global Square
    global score
    global bgphoto
    global snake
    global x
    global y
    global direction

    pygame.init()
    
    equal = False
    subtract = False
    scoretxt = pygame.font.SysFont("monospace", 30)

###xp,yp for the apple(blue circles)###
###nx, ny for the red circles (the player is not supposed to eat them###
##the others are to have more point , to make the game harder
##3 red cherries , 3 yellow cherries, 2 blue cherries
    xp = 50
    yp = 100
    nx = 200
    ny = 400
    yx = 150
    yy = 380
   
    xp2 = 60
    yp2= 40
    nx2 = 300
    ny2 = 190
    yx2 = 55
    yy2 = 55
    nx3 = 90
    ny3 = 320
    yx3 = 60
    yy3 = 20
    
    clock = pygame.time.Clock()
    
    Smode = pygame.display.set_mode((800,500))
###window's title###
    pygame.display.set_caption('Single Player')
    background = pygame.image.load(bgphoto)
    Smode.blit(background, (0,0))
    Square = pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0)
    P = pygame.draw.circle(Smode, (30,144,255), (50,100), 15, 0)
    gameExit = False
###change the position of the apple every 3 seconds###
    pygame.time.set_timer(pygame.USEREVENT+1,4000)
###loop###
    while not gameExit:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             
                pygame.quit()
                sys.exit()
                quit()
                #game exits!
        ###player's inputs : 
            if event.type == pygame.KEYDOWN:
                #change direction :
               
                if event.key == pygame.K_LEFT and direction!= 1:
                    direction = 3
                if event.key == pygame.K_RIGHT and direction!= 3:
                    direction = 1 
                if event.key == pygame.K_DOWN and direction!=2:
                    direction = 0
                if event.key == pygame.K_UP and direction!=0:
                    direction = 2
                ##pause the game 
                if event.key == pygame.K_p:
                    pause = True
                    paused()
###quit the game and go to the home page
                if event.key == pygame.K_SPACE:
                    mainwindow()
##########volume settings############
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
            ##call the functions to get the new coordinates for all cherries
            if event.type == pygame.USEREVENT+1:
                xp,yp = movePoint()
              
                nx, ny = losePoint()
                
                yx, yy = yellowpoints()
                nx2, ny2 = losePoint()
                yx2, yy2 = yellowpoints()
                nx3, ny3 = losePoint()
                yx3, yy3 = yellowpoints()
                xp2,yp2 = movePoint()
               
####change directions of the snake####
        if direction == 0:
            y = y + 28
        elif direction == 1:
            x = x + 28
        elif direction == 2:
            y = y - 28
        elif direction == 3:
            x = x - 28
        snake.append((x,y))
        snake = snake[1:]

        Smode.blit(background, (0,0))
    ##moves snake
        moveS(x,y,snake)
    ##moves the cherries
        xp,yp = points(xp,yp)
        nx, ny = loss(nx , ny)
        yx, yy = moveyellow(yx, yy)
        xp2,yp2 = points(xp2,yp2)
        nx2, ny2 = loss(nx2 , ny2)
        yx2, yy2 = moveyellow(yx2, yy2)
        nx3, ny3 = loss(nx3 , ny3)
        yx3, yy3 = moveyellow(yx3, yy3)

#####update score####
        pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
        Smode.blit(pscore, (20,20))
        
        
###if they are close, call the function (change the cherry's position)###
        ##and increase the score, (2 blue berries will be shown on the window)##
        if (abs(x - xp))< 22 and (abs(y-yp))< 22  :
            equal = True
            xp,yp = movePoint()
            score = score + 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
        if (abs(x - xp2))< 22 and (abs(y-yp2))< 22  :
            equal = True
            xp,yp = movePoint()
            score = score + 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))

###for the red berries(3 red berries)###
        if (abs(x-nx))<22 and (abs(y-ny))<22 :
            youlosewnd()
        if (abs(x-nx2))<22 and (abs(y-ny2))<22 :
            youlosewnd()
        if (abs(x-nx3))<22 and (abs(y-ny3))<22 :
            youlosewnd()
###for the rotten berries, subtract 1 point(3 rotten berries)###
            ##update the score##
        if (abs(x - yx))< 22 and (abs(y-yy))< 22  :
            subtract = True
            yx,yy = yellowpoints()
            score = score - 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
            if score < 0 :
                score = 0
                youlosewnd()
        if (abs(x - yx2))< 22 and (abs(y-yy2))< 22  :
            subtract = True
            yx2,yy2 = yellowpoints()
            score = score - 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
            if score < 0 :
                score = 0
                youlosewnd()
        if (abs(x - yx3))< 22 and (abs(y-yy3))< 22  :
            subtract = True
            yx3,yy3 = yellowpoints()
            score = score - 1
            pscore = scoretxt.render("Score: " + str(score), True, (176,48,96))
            if score < 0 :
                score = 0
                youlosewnd()

###Adding length####
        if equal == True :
            snake.append(pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0))
            equal = False
###subttract length of the snake if the player has eaten the yellow berry###
        if subtract == True :
            snake = snake[1:]
            subtract = False

#####show "you lose" window, if the snake hits the walls#####
        if x > 777 :
            youlosewnd()
        if y > 490 :
            youlosewnd()
        if x < 1 :
            youlosewnd()
        if y < -5:
            youlosewnd()
        pygame.display.update()

        
   
##moveS draws the rectangle according to the input from the user, to move the snake 
def moveS(x,y,sn):
    global Smode
    global Square
    Square = []
    for pt in sn:
        x,y = pt[0],pt[1]
        Square.append(pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0))



##this moves the second player's snake
def moveS2(x2,y2,sn2):
    global Smode
    global Square2
    Square2 = []
    for pt2 in sn2:
        x2,y2 = pt2[0],pt2[1]
        Square2.append(pygame.draw.rect(Smode, (100,50,150), (x2,y2,28,28), 0))



##chooses random x and y for the blue berry##
def movePoint():
    global P
    x = random.randint(20,770)
    y = random.randint(30, 440)
    return (x,y)

#takes the x and y from the previous funtion and moves the cherry#
def points(x,y):
    global P
    P = pygame.draw.circle(Smode, (30,144,255), (x,y), 15, 0)
    return (x,y)
##chooses random x and y for the red berries
def losePoint():
    nx = random.randint(20,700)
    ny = random.randint(30,400)
    return (nx,ny)
##moves red berries##
def loss(nx,ny):
    global NP
    NP = pygame.draw.circle(Smode, (255,0,0), (nx,ny), 15, 0)
    return (nx,ny)

##get x and y for the rotten berries##
def yellowpoints():
    yx = random.randint(20,700)
    yy = random.randint(30,400)
    return (yx,yy)
##moves the rotten berries##
def moveyellow(yx,yy):
    global YP
    YP = pygame.draw.circle(Smode, (255,255,0), (yx,yy), 15, 0)
    return (yx,yy)
    


###this function lets the player choose the background 
def choosebackground():
    global bgphoto
##https://www.pinterest.com/pin/443182419555385656/##
##http://www.spoonflower.com/fabric/##
##some photos are edited by me ##
    choosebg = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Choose Your Background')
    choice = pygame.image.load("BGs.png")
    choosebg.blit(choice, (0,0))
    gameExit = False
    basicFont = pygame.font.SysFont("arial", 40)

    ##press any letter under the photo to choose the background
    start = basicFont.render("Press J", True, (255,255,255))
    main.blit(start, (50,400))
    start = basicFont.render("Press K", True, (255,255,255))
    main.blit(start, (300,400))
    start = basicFont.render("Press L", True, (255,255,255))
    main.blit(start, (600,400))
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                gameExit = True
                sys.exit()
                quit()
                ##game exits 
            if event.type == pygame.KEYDOWN :
                ##inputs from player to choose the background##
                if event.key == pygame.K_SPACE :
                    mainwindow()
                if event.key == pygame.K_j :
                    bgphoto = "grid.png"
                    mainwindow()
                    
                if event.key == pygame.K_k :
                    bgphoto = "grid2.png"
                    mainwindow()

                if event.key == pygame.K_l :
                    bgphoto = "pinky.png"
                    mainwindow()
                if event.key == pygame.K_q :
                    gameExit = True
                    sys.exit()
                    quit()
                ##set the volume##
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
                    
        pygame.display.update()



                
                
            
####multiplayer mode window####
def MultiplayerMode():
    global pause
    global Smode
    global Square
    global score1
    global score2
    global xx
    global bgphoto
    pygame.init()
    ###setting text's size and type##
    scoretxt = pygame.font.SysFont("monospace", 30)
    score1 = 0
    score2 = 0
###for player 1 , player 2###
    snake = [(25,20),(35,20),(45,20),(55,20)]
    snake2 = [(30,35),(40,35),(50,35),(60,35)]
    ##x and y for the first snake##
  
    x = 20
    y = 20

    x2 = 100
    y2 = 100
    ##directions of the snakes in the beginning##
    direction1 = 0
    direction2 = 0
    ##coordinates of the red, rotten, and blue berries##
    xp = 200
    yp = 120
    xn = 300
    yn = 100
    yx = 444
    yy = 390
    clock = pygame.time.Clock()
    Smode = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Multiplayer')
    background = pygame.image.load(bgphoto)
    Smode.blit(background, (0,0))
###draws the snakes###
    Square = pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0)
    Square2 = pygame.draw.rect(Smode, (100,50,150), (x2,y2,28,28), 0)
    P = pygame.draw.circle(Smode, (30,144,255), (55,100), 15, 0)
    gameExit = False
    equal1 = False
    equal2 = False
    ###loop##
    pygame.time.set_timer(pygame.USEREVENT+1,4000)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                sys.exit()
                quit()
                #game exits!
#########player 1 inputs:#########
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction1!= 1:
                    direction1 = 3
                if event.key == pygame.K_RIGHT and direction1!= 3:
                    direction1 = 1 
                if event.key == pygame.K_DOWN and direction1!=2:
                    direction1 = 0
                if event.key == pygame.K_UP and direction1!=0:
                    direction1 = 2
#########player 2 inputs:#########
                if event.key == pygame.K_a and direction2!=1:
                    direction2 = 3
                if event.key == pygame.K_d and direction2!=3:
                    direction2 = 1
                if event.key == pygame.K_s and direction2!=2:
                    direction2 = 0
                if event.key == pygame.K_w and direction2!=0:
                    direction2 = 2
########pause########
                if event.key == pygame.K_p:
                    pause = True
                    paused()
###quit the game and go to the home page###
                if event.key == pygame.K_SPACE:
                    mainwindow()
####volume settings####
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
###timer to call the function to move the berries####                     
            if event.type == pygame.USEREVENT+1:
                xp,yp = movePoint()
                xn,yn = losePoint()
                yx, yy = yellowpoints()
####change x and y of the first player's snake####
        if direction1 == 0:
            y = y + 10
        elif direction1 == 1:
            x = x + 10
        elif direction1 == 2:
            y = y - 10
        elif direction1 == 3:
            x = x - 10
####change x and y of the second player's snake####
        if direction2 == 0:
            y2 = y2 + 10
        elif direction2 == 1:
            x2 = x2 + 10
        elif direction2 == 2:
            y2 = y2 - 10
        elif direction2 == 3:
            x2 = x2 - 10
##snakes' list to be changed according to the berry eaten##
        snake.append((x,y))
        snake = snake[1:]
        snake2.append((x2,y2))
        snake2 = snake2[1:]
        Smode.blit(background, (0,0))
####move snakes 1 and 2####
        moveS(x,y,snake)
        moveS2(x2,y2,snake2)
##moves the berrries##
        xp,yp = points(xp,yp)
        xn, yn = loss(xn, yn)
        yx, yy = moveyellow(yx, yy)
        P1score = scoretxt.render("Player1: " + str(score1), True, (176,48,96))
        Smode.blit(P1score, (20,20))
        P2score = scoretxt.render("Player2: " + str(score2), True, (100,50,150))
        Smode.blit(P2score,(20,45))
####if the snake1 eats the blue berry :
        if (abs(x - xp))<22 and (abs(y-yp))< 22  :
            xp,yp = movePoint()
            score1 = score1 + 1
            p1score = scoretxt.render("Player1: " + str(score1), True, (176,48,96))
            Smode.blit(P1score, (20,20))
            equal1=True
##if the snake eats the red berry :
        if (abs(x-xn))<22 and (abs(y-yn))<22 :
            global xx
            xx = 1
            playerxlose()
        if equal1 == True :
            snake.append(pygame.draw.rect(Smode, (176,48,96), (x,y,28,28), 0))
            equal1 = False
            Smode.blit(background, (0,0))
##if the snake2 eats the blue berry :
        if (abs(x2-xp))< 22 and (abs(y2-yp))< 22 :
            score2 = score2 + 1
            p2score = scoretxt.render("Player2: " + str(score2), True, (100,50,150))
            Smode.blit(P2score, (20,45))
            equal2 = True
            xp,yp = movePoint()
##if snake2 eats the red berry :
        if (abs(x2-xn))< 22 and (abs(y2-yn))< 22 :
            #global xx
            xx = 2
            playerxlose()   
        if equal2 == True :
            snake2.append(pygame.draw.rect(Smode, (100,50,150), (x2,y2,28,28), 0))
            equal2 = False
            Smode.blit(background,(0,0))
###for the rotten berries, subtract 1 point###
        ##snake 1 :
        if (abs(x - yx))< 22 and (abs(y-yy))< 22  :
            subtract = True
            yx,yy = yellowpoints()
            score1 = score1 - 1
            pscore = scoretxt.render("Player1: " + str(score1), True, (176,48,96))
            if score1 < 0 :
                xx = "1"
                score1 = 0
                playerxlose()
#####snake 2########
        if (abs(x2 - yx))< 22 and (abs(y2-yy))< 22  :
            subtract = True
            yx,yy = yellowpoints()
            score2 = score2 - 1
            pscore = scoretxt.render("Player2: " + str(score2), True, (100,50,150))
            if score2 < 0 :
                xx = "2"
                score2 = 0
                playerxlose()
###if any snake hit the wall , the player loses...
        ##player 1 
        if x > 777 :
            xx = 1
            playerxlose()
        if y > 497 :
            xx = 1
            playerxlose()
        if x < 0 :
            xx = 1
            playerxlose()
        if y < -5 :
            xx = 1
            playerxlose()
        ##player 2 
        if x2 > 777 :
            xx = 2
            playerxlose()
        if y2 > 497 :
            xx = 2
            playerxlose()
        if x2 < 0 :
            xx = 2
            playerxlose()
        if y2 <-5 :
            xx = 2
            playerxlose()
        pygame.display.update()
        clock.tick(50)
#####show the pause window, everything else stops working####
def paused():
    global pause
    global Smode
    while pause==True:
#####set the texts' size#####
        font = pygame.font.SysFont("monospace", 80)
        ffont = pygame.font.SysFont("monospace", 30)
####show the rectangle####
        rectangleP = pygame.draw.rect(Smode, (173,216,230), (100,50,600,400), 0)
####the text that will show on the window####
        text = font.render("PAUSED", True, (0,0,0))
        text1 = ffont.render("Press p to continue", True, (50,50,50))
####get events from user####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN:
####if 'p' is pressed while the game is paused, stop the pause and continue playing
                if event.key == pygame.K_p:
                    pause = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
                if event.key == pygame.K_q :
                    gameExit = True
                    sys.exit()
                    quit()
#####show text######
        Smode.blit(text, (280,200))
        Smode.blit(text1, (236, 300))
        pygame.display.update()

#####this will show for the single mode game only#####
def youlosewnd():
##http://stackoverflow.com/questions/31812433/pygame-sceen-fill-not-filling-up-the-color-properly##
    global youlose
    global score
    global bestscore

    youlose = pygame.display.set_mode((900,600))
    Background = pygame.image.load("blue2.png")
    youlose.blit(Background, (0,0))
    pygame.init()
    pygame.display.set_caption("YOU LOSE!")
    font = pygame.font.SysFont("monospace", 25)
    font2 = pygame.font.SysFont("monospace", 45)
    best = pygame.font.SysFont("monospace", 55)
###text on window###
    start = font2.render("YOU LOSE!", 1, (200,183,213))
    youlose.blit(start, (400,50))
    start = font2.render("Your Score is: " + str(score), 1, (0,255,255))
    youlose.blit(start, (370,170))
    BS = bestscore1()
    hs = best.render("BEST SCORE: " + str(BS), 1, (0,255,255))
    youlose.blit(hs, (370,300))
    start = font.render("PRESS R TO PLAY AGAIN", 1, (255,255,0))
    youlose.blit(start, (270,450))
    start = font.render("PRESS SPACE TO GO BACK TO MAIN MENU", 1,( 255,255,0))
    youlose.blit(start, (160,489))
    pygame.display.flip()
    #pygame.display.update()
    window = False
####window's loop#####
    while not window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.exit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q :
                    gameExit = True
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.key == pygame.K_SPACE :
                    mainwindow()
                if event.key == pygame.K_r :
                    SingleModeGame()

                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)


def bestscore1():
    global score
    global bestscore

    f = open("highestscore.txt", "r")

    line = f.readlines()
    if len(line) == 0:
        f = open("highestscore.txt", "w")
        f = f.write(str(score))
        bestscore = score

        return bestscore
    else:
        for bestscore in line :

            if score > int(bestscore):

                f = open("highestscore.txt", "w")
                f.write(str(score))
                bestscore = score
                return bestscore
            if score < int(bestscore) :
                return bestscore
            if score == int(bestscore) :
                return bestscore
                




        
####instructions window####
def instructionswnd():
    global Smode
    global main
###draw rectangle on the window###
    rectangleP = pygame.draw.rect(main, (224,255,255), (0,0,900,600), 0)
###set the font size and font type
    modes = pygame.font.SysFont("monospace", 25)
    other = pygame.font.SysFont("monospace", 25)
    big = pygame.font.SysFont("monospace", 50)
###text on window and blit it###
    text = big.render("Game Instructions:", 1, (0,80,200))
    main.blit(text, (138,40))
    text = big.render("_________________", 1, (0,80,200))
    main.blit(text, (138,45))
    text = modes.render("Single Mode Instructions:", 1, (50,50,150))
    main.blit(text, (70,120))
    text = modes.render("_________________________", 1, (50,50,150))
    main.blit(text, (70,125))
    text = other.render("Use the arrows keys to move", 1, (50,50,50))
    main.blit(text, (150, 160))
    text = modes.render("Multiplayer Mode Instructions:", 1, (50,50,150))
    main.blit(text, (70,190))
    text = modes.render("_____________________________", 1, (50,50,150))
    main.blit(text, (70,195))
    text = other.render("Player 1 : Use the arrow keys to move", 1, (176,48,96))
    main.blit(text, (150,230))
    text = other.render("Player 2 : Use 'a,s,d,w' to move", 1, (100,50,150))
    main.blit(text, (150,260))
    text = modes.render("PRESS P TO PAUSE THE GAME", 1, (50,50,150))
    main.blit(text, (240,300))
    text = modes.render("DO NOT TOUCH THE EDGES", 1, (50,50,150))
    main.blit(text, (250,330))
    text = modes.render("IF YOU EAT THE BLUE BERRIES , YOU'LL GAIN POINTS", 1, (0,10,255))
    main.blit(text, (80,370))
    text = modes.render("IF YOU EAT THE ROTTEN BERRIES, YOU'LL LOSE POINTS", 1, (255,140,0))
    main.blit(text, (60,410))
    text = modes.render("IF YOU EAT THE RED BERRIES, YOU'LL LOSE", 1, (200,10,20))
    main.blit(text, (100,450))

    text = modes.render("PRESS SPACE TO GO TO HOMEPAGE", 1, (50,50,150))
    main.blit(text, (220,490))
    text = modes.render("PRESS 0 to mute music", 1, (50,50,150))
    main.blit(text, (260,520))
    text = modes.render("PRESS 1 to play music", 1, (50,50,150))
    main.blit(text, (260,550))
    window = False
#### loop to show the window####
    while not window:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    window = True
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.key == pygame.K_SPACE:
                                mainwindow()
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
        pygame.display.flip()

#if any player in the multiplayer game lose this function will be called:
def playerxlose():
    global xx
    global score1
    global score2
    global highestscore
    global score
    ##add photo##
    pygame.init()
    playerL = pygame.display.set_mode((900,600))
    Background = pygame.image.load("blue2.png")
    playerL.blit(Background, (0,0))
    ##set texts sizes and font types##
    font = pygame.font.SysFont("monospace", 35)
    fontt = pygame.font.SysFont("monospace", 50)
    best = pygame.font.SysFont("monospace", 55)
###the text on window###
    start = fontt.render("PLAYER " + str(xx) +" LOST!", 1, (173,255,47))
    playerL.blit(start, (350,50))
    start = font.render("PLAYER 1 SCORE: " + str(score1), 1, (176,48,96))
    playerL.blit(start, (360,130))
    start = font.render("PLAYER 2 SCORE: " + str(score2), 1, (100,50,150))
    playerL.blit(start, (360,160))
    ##compare the scores to set the highest score in the game##
    if score1 > score2 :
        highestscore = score1

    if score1 < score2 :
        highestscore = score2

    if score1 == score2 and score1 >0 :
        highestscore = score1

    if score1==0 and score2 == 0:
        highestscore = 0

    score = highestscore
    ##calls the function to show the best score among the players##
    BS = bestscore1()
    highscore = best.render("BEST SCORE: " + str(BS), 1, (173,255,47))
    playerL.blit(highscore, (400,280))

    
    start = font.render("PRESS SPACE TO GO BACK", 1, (0,191,255))
    playerL.blit(start, (180,470))
    start = font.render("PRESS R TO PLAY AGAIN", 1, (0,191,255))
    playerL.blit(start, (180,520))
    pygame.display.flip()
    pygame.display.update()
    window = False
####window's loop#####
    while not window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.exit()
                quit()
            ##inputs from player##
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q :
                    gameExit = True
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.key == pygame.K_SPACE :
                    mainwindow()
                if event.key == pygame.K_r:
                    MultiplayerMode()
                if event.key == pygame.K_1:
                    pygame.mixer.music.set_volume(1)
                if event.key == pygame.K_0:
                    pygame.mixer.music.set_volume(0)
        playerL.fill((224,255,255))
                    

#####DONE#####
        ##enjoy playing snyko##
 
mainwindow()


