import pygame
import constantes

class Enemy:
    
    def __init__(self, screen, x,y,imagen):
        self.screen = screen
        self.x = x
        self.y = y
        self.imagen = imagen
        
        
        
        
    def Ultra_draw_le(self):
        self.imagen.set_colorkey(constantes.NEGRO)
        self.imagen = pygame.transform.scale(self.imagen,(100,100))
        self.screen.blit(self.imagen,(self.x,self.y))
        
        