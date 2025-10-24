import tkinter as tk
import pong_ai
import pong
import pygame
#Fem una variable de que estem al menú
menu = True
dificultat = 0

pygame.init()
pygame.joystick.init()


def crear_menu():
    # Configuració de la pantalla
    root = tk.Tk()
    root.title("Menu Pong")
    root.configure(bg="black") 
    root.attributes('-fullscreen', True)


    titol = tk.Label(root, text="PONG", font=("Courier", 62, "bold"),fg="white", bg="#1a1a1a")
    titol.pack(pady=45)

    # Funcions per cada partida
    # Funcions per la partida 1vs1
    def jugar_partida_curta_normal():
        root.destroy()
        menu = False
        root.after(100, lambda: pong.jugar_pong(3))


    def jugar_partida_mitjana_normal():
        root.destroy()
        menu = False
        root.after(100, lambda: pong.jugar_pong(6))

    def jugar_partida_llarga_normal():
        root.destroy()        
        menu = False
        root.after(100, lambda: pong.jugar_pong(9))

    # Funcions per jugar contra la màquina
    def jugar_partida_curta_maquina():
        root.destroy()        
        menu = False
        root.after(100, lambda: pong_ai.jugar_pong(3, dificultat))

    def jugar_partida_mitjana_maquina():
        root.destroy()        
        menu = False

        root.after(100, lambda: pong_ai.jugar_pong(6, dificultat))

    def jugar_partida_llarga_maquina():
        root.destroy()        
        menu = False
        root.after(100, lambda: pong_ai.jugar_pong(9, dificultat))

    btn_font = ("Courier", 28, "bold")
    btn_bg = "white"
    btn_fg = "black"
    btn_active_bg = "grey"



    # Crear botons
    # Creem una funció perquè el jugador trii la duració (1vs1)
    global triar_duracio_normal
    def triar_duracio_normal():
        # Primer fem desaparèixer els botons que hi havien 
        boto_normal.pack_forget()
        boto_maquina.pack_forget()
        # Botons de selecció de partida
        tk.Button(root, text="Partida curta (3 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_curta_normal).pack(pady=15)

        tk.Button(root, text="Partida mitjana (6 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_mitjana_normal).pack(pady=15)

        tk.Button(root, text="Partida llarga (9 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_llarga_normal).pack(pady=15)
        
    # Creem una funció perquè el jugador trii la duració (màquina)
    def triar_duracio_maquina():
        # Botons de selecció de partida
        tk.Button(root, text="Partida curta (3 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_curta_maquina).pack(pady=15)

        tk.Button(root, text="Partida mitjana (6 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_mitjana_maquina).pack(pady=15)

        tk.Button(root, text="Partida llarga (9 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=jugar_partida_llarga_maquina).pack(pady=15)

    # Creem una funció per triar la dificultat en cas que el jugador vulgui jugar contra la màquina
    def triar_dificultat():
        boto_normal.pack_forget()
        boto_maquina.pack_forget()
        global boto_pfacil, boto_pnormal, boto_pdificil

        boto_pfacil = tk.Button(root, text="Fàcil", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=lambda: canviar_dificultat(200))
        boto_pfacil.pack(pady=15)

        boto_pnormal = tk.Button(root, text="Normal", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=lambda: canviar_dificultat(100))
        boto_pnormal.pack(pady=15)

        boto_pdificil = tk.Button(root, text="Difícil", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=34, height=3, command=lambda: canviar_dificultat(1))        
        boto_pdificil.pack(pady=15)

    def canviar_dificultat(x):
        global dificultat
        dificultat = x
        boto_pfacil.pack_forget()
        boto_pnormal.pack_forget()
        boto_pdificil.pack_forget()
        triar_duracio_maquina()
        


    # Botons de 1vs1 o jugar contra IA
    boto_normal = tk.Button(root, text="1vs1", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=34, height=3, command=triar_duracio_normal)
    boto_normal.pack(pady=20)

    boto_maquina = tk.Button(root, text="Maquina", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=34, height=3, command=triar_dificultat)
    boto_maquina.pack(pady=20)


    for event in pygame.event.get():
        print("S'ha entrat en el bucle")
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.JOYBUTTONDOWN:
            print("S'ha clicat el botó, funciona!")  
            triar_duracio_normal()
        else:
            print("Else") 

   # Això ha d'estar al final
    root.mainloop()

crear_menu()


