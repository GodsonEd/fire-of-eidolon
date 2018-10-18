import os, sys
import pygame
from pygame.locals import *
from tkinter import *

if not pygame.font: print
'Warning, fonts disabled'
if not pygame.mixer: print
'Warning, sound disabled'

"""
Import modules
set up game( difficulty  ) 
"""

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fire of Eidolon')
pygame.mouse.set_visible(1)

backgroundImage = pygame.image.load("Textures/intro.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
screen.blit(backgroundImage, (0, 0))
# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((250,250,250))

clock = pygame.time.Clock()
done = False

# if pygame.font:
# font = pygame.font.Font(None, 50)
# text = font.render("Fire of Eidolon", 1 (10,10,10))
# textpos = text.get_rect(centerx = background.get_width()/2)
# background.blit(text,textpos)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except ValueError:
        print('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect


def load_sound(name):
    return


while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True


    pygame.display.flip()
