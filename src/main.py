from debug import print_debug
from level import Level
import settings

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            self.screen.fill("black")
            pygame.display.update()
            self.level.run()
            self.clock.tick(settings.FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
