import pygame

def pantalla_final(guanyador, puntuacio_max):
    pygame.init()
    pygame.joystick.init()
    pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Jugador guanyador")


    def reiniciar():
        import pong_ai
        import menu_pong
        pygame.display.quit()
        pong_ai.jugar_pong(puntuacio_max, menu_pong.dificultat)

    def tornar_menu():
        import menu_pong
        pygame.display.quit()
        menu_pong.crear_menu()



    font_titol = pygame.font.SysFont("Courier", 100, bold=True)
    titol_surface = font_titol.render(f"JUGADOR {guanyador} GUANYADOR", True, (255, 255, 255))
    titol_rect = titol_surface.get_rect(center=(pantalla.get_width() // 2, 100))
    pantalla.blit(titol_surface, titol_rect)


    boto_reiniciar = {"rect": pygame.Rect(380, 220, 600, 140), "text": "Reiniciar"}
    boto_menu = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Tornar al menú"}
    # Dibuixa tots els botons

    running = True
    while running: 
        print("S'ha entrat en el bucle")       
        for boto in [boto_reiniciar, boto_menu]:
            pygame.draw.rect(pantalla, "white", boto["rect"])
            text = pygame.font.SysFont("Courier", 28, bold=True).render(boto["text"], True, "black")
            pantalla.blit(text, text.get_rect(center=boto["rect"].center))
            print("S'han dibuixat els botons")


        pygame.display.flip()  # <-- Actualitza la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("S'ha tancat la palanca")
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                print("Boto detectat")
                if event.button == 1 or event.button == 3:
                    reiniciar()
                    running = False
                elif event.button == 0 or event.button == 2:
                    tornar_menu()
                    running = False
            else:
                print("else")

        pygame.time.Clock().tick(60)
    print("cfghjk")

    #pygame.quit()
