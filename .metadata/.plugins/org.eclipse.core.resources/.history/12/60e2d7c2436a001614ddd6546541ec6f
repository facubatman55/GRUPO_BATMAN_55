import pygame
from Enemigos import Enemy 

import constantes
from jugador import Player

""" Clase principal en el que se debe ejecutar el juego. """
pygame.init()
x= 600
y=300
# Configuramos el alto y largo de la pantalla
size = [constantes.ANCHO_PANTALLA, constantes.ALTURA_PANTALLA]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Proyecto Video-Juegos")

# Creamos al jugador con la imagen p1_walk.png
jugador_principal = Player("imagenes/p1_walk.png")
jugador_principal.rect.x = 0
#jugador_principal.rect.y = constantes.ALTURA_PANTALLA - jugador_principal.rect.height
jugador_principal.rect.y = 300


lista_sprites_activos = pygame.sprite.Group()
lista_sprites_activos.add(jugador_principal)

#Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
salir = False

clock = pygame.time.Clock()

# -------- Loop Princiapl -----------
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


    # Actualiza todo el jugador
    screen.fill(constantes.AZUL)
    lista_sprites_activos.update()
    
    
    
    llayer_imagen= pygame.image.load("imagenes/Rifleman_pic.png").convert()
    bios = Enemy(screen,x,y, llayer_imagen)
    bios.Ultra_draw_le()

    # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
    lista_sprites_activos.draw(screen)

    # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.

    clock.tick(60)

    pygame.display.flip()

pygame.quit()

