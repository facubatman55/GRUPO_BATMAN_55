import pygame
from funciones_spritesheet import SpriteSheet
import constantes

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, ruta):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)        
        sprite_sheet = SpriteSheet(ruta)       
        
        # recorte de la imagen de acuerdo a sus dimensiones
        self.image = sprite_sheet.obtener_imagen_enemigo(0, 0, 70, 80)
        
        # si hay que escalar imagen o transparentar un color se debe hacer aca 
                
        self.rect = self.image.get_rect()    
    