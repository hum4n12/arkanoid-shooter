import pygame

class Utils:        
    font = None
    surface = None
    surfaces = []

    @staticmethod
    def Print(text: str) -> None:
            text_surface = Utils.font.render(text, True, (255, 255, 255))
            Utils.surface.blit(text_surface, text_surface.get_rect(center=(1000, 500)))
    
    @staticmethod
    def Vec_to_tuple(vec: pygame.Vector2) -> tuple[int, int]:
          return (vec.x, vec.y)
