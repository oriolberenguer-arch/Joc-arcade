import pong_ai
import pong
import pygame
import sys
#Fem una variable de que estem al menú
menu = True
dificultat = 0

def crear_menu():
    pygame.init()
    pygame.joystick.init()
    pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Menu Pong")

    # Configuració de la pantalla
    font_titol = pygame.font.SysFont("Courier", 100, bold=True)
    titol_surface = font_titol.render("PONG", True, (255, 255, 255))
    titol_rect = titol_surface.get_rect(center=(pantalla.get_width() // 2, 100))
    pantalla.blit(titol_surface, titol_rect)

    # Funcions per cada partida
    # Funcions per la partida 1vs1
    def jugar_partida_curta_normal():
        global menu
        menu = False
        #pygame.display.quit()
        pong.jugar_pong(3)


    def jugar_partida_mitjana_normal():
        global menu
        menu = False
        #pygame.display.quit()
        pong.jugar_pong(6)

    def jugar_partida_llarga_normal():
        global menu
        menu = False
        #pygame.display.quit()
        pong.jugar_pong(9)

    # Funcions per jugar contra la màquina
    def jugar_partida_curta_maquina():
        global menu
        menu = False
        pong_ai.jugar_pong(1, dificultat)
        pygame.quit()


    def jugar_partida_mitjana_maquina():
        global menu
        menu = False
        #pygame.display.quit()
        pong_ai.jugar_pong(6, dificultat)

    def jugar_partida_llarga_maquina():
        global menu
        menu = False
        #pygame.display.quit()
        pong_ai.jugar_pong(9, dificultat)

    btn_font = pygame.font.SysFont("Courier", 28, bold=True)
    btn_bg = "white"
    btn_fg = "black"
    btn_active_bg = "grey"

    # Crear botons
    # Creem una funció perquè el jugador trii la duració (1vs1)
    global triar_duracio_normal
    def triar_duracio_normal():
        boto_partida_curta = {"rect": pygame.Rect(380, 220, 600, 140), "text": "Partida curta (3 punts)"}
        boto_partida_mitjana = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Partida mitjana (6 punts)"}
        boto_partida_llarga = {"rect": pygame.Rect(380, 560, 600, 140), "text": "Partida llarga (9 punts)"}
        running = True
        while running:
            for boto in [boto_partida_curta, boto_partida_mitjana, boto_partida_llarga]:
                pygame.draw.rect(pantalla, btn_bg, boto["rect"])
                text = btn_font.render(boto["text"], True, btn_fg)
                pantalla.blit(text, text.get_rect(center=boto["rect"].center))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        jugar_partida_curta_normal()
                        running = False
                    elif event.button == 2:
                        jugar_partida_mitjana_normal()
                        running = False
                    elif event.button == 3:
                        jugar_partida_llarga_normal()
                        running = False
        
    # Creem una funció perquè el jugador trii la duració (màquina)
    def triar_duracio_maquina():
        boto_partida_curta_maquina = {"rect": pygame.Rect(380, 220, 600, 140), "text": "Partida curta (3 punts)"}
        boto_partida_mitjana_maquina = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Partida mitjana (6 punts)"}
        boto_partida_llarga_maquina = {"rect": pygame.Rect(380, 560, 600, 140), "text": "Partida llarga (9 punts)"}
        running = True
        while running:
            for boto in [boto_partida_curta_maquina, boto_partida_mitjana_maquina, boto_partida_llarga_maquina]:
                pygame.draw.rect(pantalla, btn_bg, boto["rect"])
                text = btn_font.render(boto["text"], True, btn_fg)
                pantalla.blit(text, text.get_rect(center=boto["rect"].center))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        jugar_partida_curta_maquina()
                        running = False
                    elif event.button == 2:
                        jugar_partida_mitjana_maquina()
                        running = False
                    elif event.button == 3:
                        jugar_partida_llarga_maquina()
                        running = False
    # Creem una funció per triar la dificultat en cas que el jugador vulgui jugar contra la màquina
    def triar_dificultat():
        boto_pfacil = {"rect": pygame.Rect(380, 220, 600, 140), "text": "Fàcil"}
        boto_pnormal = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Normal"}
        boto_pdificil= {"rect": pygame.Rect(380, 560, 600, 140), "text": "Difícil"}
        running = True
        while running:
            for boto in [boto_pfacil, boto_pnormal, boto_pdificil]:
                pygame.draw.rect(pantalla, btn_bg, boto["rect"])
                text = btn_font.render(boto["text"], True, btn_fg)
                pantalla.blit(text, text.get_rect(center=boto["rect"].center))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        canviar_dificultat(200)
                        running = False
                    elif event.button == 2:
                        canviar_dificultat(100)
                        running = False
                    elif event.button == 3:
                        canviar_dificultat(1)
                        running = False


    def canviar_dificultat(x):
        global dificultat
        dificultat = x
        triar_duracio_maquina()
        


    # Botons de 1vs1 o jugar contra IA
    boto_normal = {"rect": pygame.Rect(380, 220, 600, 140), "text": "1vs1"}
    boto_maquina = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Maquina"}
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    running = True
    while running:
        for boto in [boto_normal, boto_maquina]:
            pygame.draw.rect(pantalla, btn_bg, boto["rect"])
            text = btn_font.render(boto["text"], True, btn_fg)
            pantalla.blit(text, text.get_rect(center=boto["rect"].center))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0 or event.button == 2:
                    triar_dificultat()
                    running = False
                elif event.button == 1 or event.button == 3:
                    triar_duracio_normal()
                    running = False


crear_menu()
