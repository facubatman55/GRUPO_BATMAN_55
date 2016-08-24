import pygame

import constantes


from funciones_spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    """Clase utilizada para desarrollar los jugadores del juego. """
    
    # -- Atributos
    mover_x = 0
    mover_y = 0

    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []

    # Direccion en la que va el jugador.
    direccion = "R"


    # -- Metodos
    def __init__(self,ruta):
        """ __Funcion constructor__ 
            Aca en donde se debe cargar el sprite sheet del jugador.
            Se debe cargar los sprite con movimiento hacia la izquierda y hacia la derecha.
        """
        
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(ruta)
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        #1
        imagen = sprite_sheet.obtener_imagen(0, 0, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #2
        imagen = sprite_sheet.obtener_imagen(66, 0, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #3
        imagen = sprite_sheet.obtener_imagen(132, 0, 67, 90)
        self.jugador_frame_der.append(imagen)
        
        #7
        imagen = sprite_sheet.obtener_imagen(0, 93, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #8
        imagen = sprite_sheet.obtener_imagen(66, 93, 66, 90)
        self.jugador_frame_der.append(imagen)
        
        #9
        imagen = sprite_sheet.obtener_imagen(132, 93, 72, 90)
        self.jugador_frame_der.append(imagen)
        
        #10
        imagen = sprite_sheet.obtener_imagen(0, 186, 70, 90)
        self.jugador_frame_der.append(imagen)

        # # Carga de todos los sprite de la imagen hacia la derecha y la rotamos.
        imagen = sprite_sheet.obtener_imagen(0, 0, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(66, 0, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(132, 0, 67, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(0, 93, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(66, 93, 66, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(132, 93, 72, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)
        imagen = sprite_sheet.obtener_imagen(0, 186, 70, 90)
        imagen = pygame.transform.flip(imagen, True, False)
        self.jugador_frame_izq.append(imagen)

        # Seteamos con que sprite comenzar
        self.image = self.jugador_frame_der[0]


        self.rect = self.image.get_rect()
        

    def update(self):
        """ Metodo que actualiza la posicion del jugador. """        

        # Movimientos Izquierda/Derecha
        self.rect.x += self.mover_x        
        #pos = self.rect.x + self.nivel.posicion_jugador_nivel
        pos = self.rect.x 
        if self.direccion == "R":            
            index = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[index]
        else:
            index = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[index]   
      
        self.rect.y += self.mover_y
      

    def retroceder(self):
        """ Se llama cuando movemos hacia la izq. """       
        self.mover_x = -6
        self.direccion = "L"

    def avanzar(self):
        """ Se llama cuando movemos hacia la der. """        
        self.mover_x = 6
        self.direccion = "R"
        
    def bajar(self):
        """ Se llama cuando movemos hacia la bajar. """       
        self.mover_y = 8
        

    def subir(self):
        """ Se llama cuando movemos hacia la subir. """        
        self.mover_y = -8
        
    def parar(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0
        self.mover_y = 0
