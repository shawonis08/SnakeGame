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