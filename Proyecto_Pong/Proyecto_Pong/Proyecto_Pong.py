import pygame
from pygame.locals import *    # Nuevo en la version 0.03
 
pygame.init()

#Iniciar variables de configuración del Juego

ancho = 800
alto = 600
velocidadX = 500
velocidadX2 = 3
velocidadY = 500
velocidadY2 = 3
terminado = False
reloj = pygame.time.Clock()
score_Jugador1 = 0
score_Jugador2 = 0

letra30 = pygame.font.SysFont("ERGOB.TTF", 30)

pantalla = pygame.display.set_mode( (ancho, alto) )
pygame.key.set_repeat(1,25)    

#Se establecen los valores de los objetos del juego (menu de inicio, jugadores y pelota)

imagenNave = pygame.image.load("paleta.png")    
rectanguloNave = imagenNave.get_rect()       
rectanguloNave.left = 0                
rectanguloNave.top = 0 

imagen = pygame.image.load("ballRoja.png")
rectanguloImagen = imagen.get_rect()
rectanguloImagen.left =  ancho / 2
rectanguloImagen.top = alto / 2

imagen2 = pygame.image.load("ballAzul.png")


imagenNave2 = pygame.image.load("paleta2.png")    
rectanguloNave2 = imagenNave.get_rect()       
rectanguloNave2.left = 0                
rectanguloNave2.top = 0                 

imagenPresent = pygame.image.load("titlePong.png")
rectanguloPresent = imagenPresent.get_rect()
rectanguloPresent.top = 0
rectanguloPresent.left = 0

ganaJugador1 = pygame.image.load("GanaJugador1.png")
winPlayer1 = ganaJugador1.get_rect()
winPlayer1.top = 0
winPlayer1.left = 0

ganaJugador2 = pygame.image.load("GanaJugador2.png")
winPlayer2 = ganaJugador2.get_rect()
winPlayer2.top = 0
winPlayer2.left = 0
 
partidaEnMarcha = True 

while partidaEnMarcha:                             
 
    # ---- Presentacion ----
    pantalla.fill( (0,0,0) )                        
    pantalla.blit(imagenPresent, rectanguloPresent) 
    pygame.display.flip()                           
 
    entrarAlJuego = False                           
    while not entrarAlJuego:                        
        pygame.time.wait(100)                       
        for event in pygame.event.get(KEYUP):       
            if event.key == K_SPACE:                
                entrarAlJuego = True                
 
    # ---- Comienzo de una sesion de juego ----
    rectanguloNave.left = 70                   
    rectanguloNave.top = 10                    
 
    rectanguloNave2.left = 700                  
    rectanguloNave2.top = 10                    

    ufoVisible = True
    terminado = False
    score_Jugador1 = 0
    score_Jugador2 = 0

    while not terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: terminado = True
 
        keys = pygame.key.get_pressed()                  
        
        if score_Jugador1 == 10:
            terminado = True
        if score_Jugador2 == 10:
            terminado = True

        if rectanguloImagen.colliderect(rectanguloNave):
            velocidadX2 = -velocidadX2


        if rectanguloImagen.colliderect(rectanguloNave2):
            velocidadX2 = -velocidadX2

        #Comprobar si hay Gol                     

        if rectanguloImagen.left == 1:
            score_Jugador2 += 1
            rectanguloImagen.left =  ancho / 2
            rectanguloImagen.top = alto / 2
            

        if rectanguloImagen.left == 763:
            score_Jugador1 += 1
            rectanguloImagen.left =  ancho / 2
            rectanguloImagen.top = alto / 2
            
            #Establecer movimiento y límites de escena del jugador 1 y 2

        if rectanguloNave.top >= 0:
            if keys[K_w]:                         
                rectanguloNave.top -= 4             
        
        if rectanguloNave.top <= 500:
            if keys[K_s]:                        
                rectanguloNave.top += 4

        if rectanguloNave2.top >= 0:
            if keys[K_UP]:                         
                rectanguloNave2.top -= 4             
        
        if rectanguloNave2.top <= 500:
            if keys[K_DOWN]:                        
                rectanguloNave2.top += 4             
    
        rectanguloImagen.left += velocidadX2                   
        rectanguloImagen.top += velocidadY2                    
        
        if rectanguloImagen.left < 0 or rectanguloImagen.right > ancho:
            velocidadX2 = -velocidadX2                          
        if rectanguloImagen.top < 0 or rectanguloImagen.bottom > alto:
            velocidadY2 = -velocidadY2                          
 
        pantalla.fill( (0,0,0) )                
        pantalla.blit(imagen, rectanguloImagen)
        
        pantalla.blit(imagenNave, rectanguloNave)    
        pantalla.blit(imagenNave2, rectanguloNave2)
        
        imagenPuntos = letra30.render(str(score_Jugador1)+' - '+str(score_Jugador2), True, (0,255,0), (0,0,0) )                   # Nuevo 0.10
        rectanguloPuntos = imagenPuntos.get_rect()           
        rectanguloPuntos.left = ancho / 2                           
        rectanguloPuntos.top = 10                            
        pantalla.blit(imagenPuntos, rectanguloPuntos)

        pygame.display.flip()

        # ---- Ralentizar hasta 40 fotogramas por segundo  ----
        reloj.tick(40)
        
    
    
    if score_Jugador1 == 10:
        pantalla.fill( (0,0,0) )                        
        pantalla.blit(ganaJugador1, winPlayer1) 
        pygame.display.flip()
        pygame.time.wait(3000)
    if score_Jugador2 == 10:
        pantalla.fill( (0,0,0) )                        
        pantalla.blit(ganaJugador2, winPlayer2)
        pygame.display.flip()
        pygame.time.wait(3000)
        
pygame.quit()