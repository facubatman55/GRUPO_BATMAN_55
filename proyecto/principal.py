import pygame
from Enemigos import Enemy 

import constantes
from jugador import Player

pygame.init()
x= 600
y=30
size = [constantes.ANCHO_PANTALLA, constantes.ALTURA_PANTALLA]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Proyecto Video-Juegos")

jugador_principal = Player("imagenes/p1_walk.png")
jugador_principal.rect.x = 0
jugador_principal.rect.y = 300


lista_sprites_activos = pygame.sprite.Group()
lista_sprites_activos.add(jugador_principal)

salir = False

clock = pygame.time.Clock()

while not salir:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            salir = True 

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_principal.retroceder()
                
            if evento.key == pygame.K_DOWN:
                jugador_principal.bajar()
                
            if evento.key == pygame.K_UP:
                jugador_principal.Subir()
                                                              
            if evento.key == pygame.K_RIGHT:
                jugador_principal.avanzar()
            elif evento.key == pygame.K_UP:
                y_speed= -3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT :
                jugador_principal.parar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.parar()
            if evento.key == pygame.K_UP:
                jugador_principal.parar()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.parar()


    screen.fill(constantes.AZUL)
    lista_sprites_activos.update()
    
    
    
    llayer_imagen= pygame.image.load("imagenes/Rifleman_pic.png").convert()
    bios = Enemy(screen,x,y, llayer_imagen)
    bios.Ultra_draw_le()

    lista_sprites_activos.draw(screen)


    clock.tick(60)

    pygame.display.flip()

pygame.quit()

