import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()
joyohjoy = pygame.joystick.Joystick(0)
joyohjoy.init()
hat_number = joyohjoy.get_numhats()
print (pygame.joystick.get_count())
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
	    joyohjoy.quit()
            pygame.quit()
            sys.exit()
    print(joyohjoy.get_hat(hat_number-1))
    pygame.display.update()     
    
