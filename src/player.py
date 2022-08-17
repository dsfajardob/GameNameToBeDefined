from typing import Any
import pygame
from settings import *
from pygame.math import Vector2
from pygame import Rect, Surface
from pygame.sprite import Group

class Player(pygame.sprite.Sprite):

    def __init__(self, pos: Vector2, group: Group) -> None:
        """Create the graphics and the movement for the player

        Args:
            pos (Group): Sprites group to be assosiate
            group (Vector2): Vector position where the player will start the game
        """
        super().__init__(group)

        #image setup
        self.image: Surface = pygame.Surface((32,64))
        self.image.fill("red")
        self.rect: Rect = self.image.get_rect(center=pos)

        #movement setup
        self.direction: Vector2 = pygame.math.Vector2()
        self.pos: Vector2 =  pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self) -> None:
        """Manage the user input and set the direction bassed on it
        """
        keys = pygame.key.get_pressed()

        # horizontal
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1 
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # vertical
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt: float) -> None:
        """Move the player with frame rate independency

        Args:
            dt (float): Time between one frame and other
        """

        # normalize to prevent faster diagonal movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # set horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # set vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        
        print(self.direction)


    def update(self, dt: float) -> None:
        """Handle the input and the movement

        Args:
            dt (float): Time between one frame and other
        """
        self.input()
        self.move(dt=dt)
