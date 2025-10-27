import pygame

pygame.init()


def pantalla_final(guanyador, puntuacio_max):
    pygame.init()
    pygame.joystick.init()
    pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Jugador guanyador")


    def reiniciar():
        import pong
        pygame.display.quit()
        pong.jugar_pong(puntuacio_max)

    def tornar_menu():
        import menu_pong     
        menu_pong.crear_menu()


    font_titol = pygame.font.SysFont("Courier", 100, bold=True)
    titol_surface = font_titol.render(f"JUGADOR {guanyador} GUANYADOR", True, (255, 255, 255))
    titol_rect = titol_surface.get_rect(center=(pantalla.get_width() // 2, 100))
    


    boto_reiniciar = {"rect": pygame.Rect(380, 220, 600, 140), "text": "Reiniciar"}
    boto_menu = {"rect": pygame.Rect(380, 390, 600, 140), "text": "Tornar al menú"}
    running = True
    while running:
        pantalla.fill((0, 0, 0))
        pantalla.blit(titol_surface, titol_rect)
        for boto in [boto_reiniciar, boto_menu]:
            pygame.draw.rect(pantalla, "white", boto["rect"])
            text = pygame.font.SysFont("Courier", 28, bold=True).render(boto["text"], True, "black")
            pantalla.blit(text, text.get_rect(center=boto["rect"].center))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1 or event.button == 3:
                        reiniciar()
                        running = False
                    elif event.button == 0 or event.button == 2:
                        running = False
                        tornar_menu()
        pygame.display.flip()
