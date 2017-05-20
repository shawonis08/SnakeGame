# pygame sound & graphics
import pygame as p
# sys -> System exit the program
import sys
# time sleep & message display
import time
# random for different coordinate
import random

# check pygame initalize return value
# print(pygame.init())

# apply condition based on initialize value
check_errors = p.init()
# (6, 0)
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors,"
          "exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Game initializing Succesfully")

# Game Screen
# changing window name
p.display.set_caption("Snake Game")
# gamescreen width,height initialize but function accept one parameter
gamescreen = p.display.set_mode((720, 460))
# hold the gamescreen
time.sleep(2)

# set Color for Game
red = p.Color(255,0,0) #gameover
green = p.Color(0,255,0) #snake
blue = p.Color(0,0,255) #score
white = p.Color(255,255,255) #screen
yellow = p.Color(255,255,224) #food

# FPS controller
fpscontroller = p.time.clock()

# Game variable
snakepostiton = [100,50]
snakebody = [[100,50],[90,50],[80,50]]

#food variable & random position
foodposition = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodpopup = True

move = 'RIGHT'
chagemove = move
