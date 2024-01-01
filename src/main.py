from debug import print_debug
import settings

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.fill("black")
                    return
                pygame.display.update()
                self.clock.tick(settings.FPS)
                print_debug(settings.FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
