import tkinter as tk
import pong_ai
import pong

#Fem una variable de que estem al menú
menu = True

def crear_menu():
    # Configuració de la pantalla
    root = tk.Tk()
    root.title("Menu Pong")
    root.geometry("800x600")
    root.configure(bg="black") 
    # codi real--> wn._root.attributes('-fullscreen', True)


    titol = tk.Label(root, text="PONG", font=("Courier", 36, "bold"),fg="white", bg="#1a1a1a")
    titol.pack(pady=30)

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
        root.after(100, lambda: pong_ai.jugar_pong(3))

    def jugar_partida_mitjana_maquina():
        root.destroy()        
        menu = False

        root.after(100, lambda: pong_ai.jugar_pong(6))

    def jugar_partida_llarga_maquina():
        root.destroy()        
        menu = False
        root.after(100, lambda: pong_ai.jugar_pong(9))

    btn_font = ("Courier", 16, "bold")
    btn_bg = "white"
    btn_fg = "black"
    btn_active_bg = "grey"


    # Crear botons
    # Creem una funció perquè el jugador trii la duració (1vs1)
    def triar_duracio_normal():
        # Primer fem desaparèixer els botons que hi havien 
        boto_normal.pack_forget()
        boto_maquina.pack_forget()
        # Botons de selecció de partida
        tk.Button(root, text="Partida curta (3 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_curta_normal).pack(pady=10)

        tk.Button(root, text="Partida mitjana (6 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_mitjana_normal).pack(pady=10)

        tk.Button(root, text="Partida llarga (9 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_llarga_normal).pack(pady=10)
        
    # Creem una funció perquè el jugador trii la duració (màquina)
    def triar_duracio_maquina():
        # Primer fem desaparèixer els botons que hi havien 
        boto_normal.pack_forget()
        boto_maquina.pack_forget()
        # Botons de selecció de partida
        tk.Button(root, text="Partida curta (3 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_curta_maquina).pack(pady=10)

        tk.Button(root, text="Partida mitjana (6 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_mitjana_maquina).pack(pady=10)

        tk.Button(root, text="Partida llarga (9 punts)", font=btn_font,
                bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                width=25, height=2, command=jugar_partida_llarga_maquina).pack(pady=10)



    # Botons de 1vs1 o jugar contra IA
    boto_normal = tk.Button(root, text="1vs1", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=25, height=2, command=triar_duracio_normal)
    boto_normal.pack(pady=10)

    boto_maquina = tk.Button(root, text="Maquina", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=25, height=2, command=triar_duracio_maquina)
    boto_maquina.pack(pady=10)


    



    # Això ha d'estar al final
    root.mainloop()
crear_menu()

