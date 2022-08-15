from json.tool import main
import pygame, sys
from settings import * 

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WITDTH, SCREEN_HEIGHT)) 
        self.clock = pygame.time.Clock()
    
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
            
            dt = self.clock.tick() / 1000
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

