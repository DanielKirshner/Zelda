from typing import Any
import pygame

@staticmethod
def print_debug(data_to_print: Any ,y: int = 10, x: int = 10) -> None:
    """
    Debug util to print debug messages in the screen  
   
    Args:
        data_to_print (Any): Message content to print.
        y (int, optional): Y Coordinate, Defaults to 10.
        x (int, optional): X Coordinate, Defaults to 10.
    """
    font = pygame.font.Font(None, 30)
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(data_to_print), True, "White")
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, "Black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)
