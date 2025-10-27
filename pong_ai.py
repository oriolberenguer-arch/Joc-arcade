import random
import pong_ai_final
import pygame
pygame.init()
pygame.joystick.init()
joysticks = []

for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)

def jugar_pong(puntuacio_max, dificultat):
    # Configuració de la pantalla
    pygame.init()
    pygame.joystick.init()
    pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pantalla.fill((0, 0, 0))
    pygame.display.set_caption("Pong")
    pygame.display.flip()

    amplada, altura = pygame.display.get_surface().get_size()

    # Configuració pales i pilota
    pala1 = pygame.Rect(0, 0, 15, 150)
    pala1.center = (100, altura // 2)
    pygame.draw.rect(pantalla, (255, 255, 255), pala1)
    pygame.display.flip()

    pala2 = pygame.Rect(0, 0, 15, 150)
    pala2.center = (amplada - 100, altura // 2)
    pygame.draw.rect(pantalla, (255, 255, 255), pala2)
    pygame.display.flip()

    bola = pygame.Rect(0, 0, 27, 27)
    bola.center = (amplada // 2, altura // 2)
    bola_dx = 3.5
    bola_dy = 3.5
    pygame.draw.rect(pantalla, (255, 255, 255), bola)
    pygame.display.flip()

    # Puntuació
    pygame.font.init()
    puntuacio1 = 0
    puntuacio2 = 0
    font = pygame.font.SysFont("courier", 36)
    texto = font.render(f"Jugador 1: {puntuacio1}          Jugador 2: {puntuacio2}", True, (255, 255, 255))
    text_rect = texto.get_rect(center=(amplada // 2, 50))
    pantalla.blit(texto, text_rect)
    #pygame.display.flip()


    # Funció per moure les pales
    def pala1_amunt():
        pala1.y -= 20
        if pala1.top < 0:
            pala1.top = 0


    def pala1_avall():
        pala1.y += 20
        if pala1.bottom > altura:
            pala1.bottom = altura

    def pala2_amunt():
        pala2.y -= 20  
        if pala2.top < 0:
            pala2.top = 0

    def pala2_avall():
        pala2.y += 20 
        if pala2.bottom > altura:
            pala2.bottom = altura



    # Bucle principal
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    x = True
    while x:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.JOYAXISMOTION:
                axis_y1 = joysticks[1].get_axis(1)
                if axis_y1 < -0.5:  # cap amunt (valor negatiu)
                    pala1_amunt()
                elif axis_y1 > 0.5:  # cap avall (valor positiu)
                    pala1_avall()
                    

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.joy == 1:
                    if event.button == 0 or event.button == 2:
                        pala1_avall()
                    elif event.button == 1 or event.button == 3:
                        pala1_amunt()
            else:
                print("peruan")

        axis_y1 = joysticks[1].get_axis(1)

        if axis_y1 < -0.5:
            pala1_amunt()
        elif axis_y1 > 0.5:
            pala1_avall()

        pygame.time.Clock().tick(50)


        pantalla.fill((0,0,0))
        pygame.draw.rect(pantalla, (255,255,255), pala1)
        pygame.draw.rect(pantalla, (255,255,255), pala2)
        pygame.draw.rect(pantalla, (255,255,255), bola)
        # Actualitzar marcador cada frame
        texto = font.render(f"Jugador 1: {puntuacio1}          Jugador 2: {puntuacio2}", True, (255, 255, 255))
        text_rect = texto.get_rect(center=(amplada // 2, 50))

        pantalla.blit(texto, text_rect)
        pygame.display.flip()


        pygame.time.Clock().tick(50)
        bola.x += bola_dx
        bola.y += bola_dy    

        # Moviment de la IA
        if bola.x > 100:
            error = random.randint(-dificultat, dificultat)  # com més gran, més fàcil
            if bola.y > pala2.y + 10 + error:
                pala2.y += 12 
            elif bola.y < pala2.y - 10 + error:
                pala2.y -= 12

        # Rebot amb parets superior/inferior
        if bola.top <= 0 or bola.bottom >= altura:
            bola_dy = -bola_dy

        if bola.left <= 0 or bola.right >= amplada:
            bola.center = (amplada // 2, altura // 2)
            bola_dx *= -1

        # Punt per jugador 1
        if bola.right >= (amplada-20):
            puntuacio1 += 1
            
            velocitat_base = 3.5
            augment = (puntuacio1 + puntuacio2) / 4
            bola_dx = -bola_dx
            
            if bola_dx > 0:
                bola_dx = velocitat_base + augment
                bola_dy = velocitat_base + augment
            else:
                bola_dx = -velocitat_base - augment
                bola_dy = -velocitat_base - augment
            
            texto = font.render(f"Jugador 1: {puntuacio1}          Jugador 2: {puntuacio2}", True, (255, 255, 255))
            text_rect = texto.get_rect(center=(amplada // 2, 50))
            bola.center = (amplada // 2, altura // 2)

        # Punt per jugador 2
        if bola.left <= 20:
            puntuacio2 += 1

                        
            velocitat_base = 3.5
            augment = (puntuacio1 + puntuacio2) / 4
            bola_dx = -bola_dx
            
            if bola_dx > 0:
                bola_dx = velocitat_base + augment
                bola_dy = velocitat_base + augment
            else:
                bola_dx = -velocitat_base - augment
                bola_dy = -velocitat_base - augment
            
            # Actualizar marcador
            texto = font.render(f"Jugador 1: {puntuacio1}          Jugador 2: {puntuacio2}", True, (255, 255, 255))
            text_rect = texto.get_rect(center=(amplada // 2, 50))
            bola.center = (amplada // 2, altura // 2)

        # Comprovació final del joc
        if puntuacio1 == puntuacio_max or puntuacio2 == puntuacio_max:
            bola_dx = 0
            bola_dy = 0

            pantalla.fill((0, 0, 0))
            #pygame.display.flip()

            if puntuacio1 == puntuacio_max:
                pong_ai_final.pantalla_final("1", puntuacio_max)
            else:
                pong_ai_final.pantalla_final("2", puntuacio_max)

            x = False

        # Xoc pilota - pala1
        if bola.colliderect(pala1):
            bola_dx *= -1.15
            bola_dy *= 1.15
            bola.left = pala1.right 

        # Xoc pilota - pala2
        elif bola.colliderect(pala2):
            bola_dx *= -1.15
            bola_dy *= 1.15
            bola.right = pala2.left 


    pygame.display.flip()
