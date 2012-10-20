'''
Created on 18 oct. 2012

@author: Edooby
'''
import pygame

class Tank:
    def __init__(self):
        self.image = pygame.image.load("tank.png")
        self.rect = self.image.get_rect()