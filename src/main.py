import pygame, sys
from settings import * 
from constants import GAME_NAME
from level import Level

class Game:
    def __init__(self) -> None:
        """Start the game.
        Here it's initialized the game window, it's setted the window title, the game clock used for delta time
        and the main level
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WITDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    def run(self) -> None:
        """Method in charge of the game loop
        """

        while True:
            # Check for quitting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
            #Call the level using the delta time
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            # Update the display with the last render
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

