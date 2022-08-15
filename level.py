import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):

        # Get display surface
        self.display_sourface = pygame.display.get_surface()
        # sprite groups 
        self.all_sprites = pygame.sprite.Group()

        #setup
        self.setup()

    def setup(self):
        self.player = Player(pos=(640,360), group=self.all_sprites)

    def run(self, dt):

        self.display_sourface.fill("white")
        self.all_sprites.draw(self.display_sourface)
        self.all_sprites.update(dt)