from settings import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.fill('black')
                    return
                pygame.display.update()
                self.clock.tick(FPS)
                    
                    
if __name__ == "__main__":
    game = Game()
    game.run()
