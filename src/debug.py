from typing import Any
import pygame

pygame.init()
font = pygame.font.Font(None, 30)
 
def debug(info: Any ,y: int = 10, x: int = 10) -> None:
    """
    Debug util to print debug info messages in the screen  
    Args:
        info (_type_): _description_
        y (int, optional): _description_. Defaults to 10.
        x (int, optional): _description_. Defaults to 10.
    """
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)