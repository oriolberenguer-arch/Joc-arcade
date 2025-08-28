import turtle
import tkinter as tk
import os
import pong
import subprocess

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
    def jugar_partida_curta():
        root.destroy()
        root.after(100, lambda: pong.jugar_pong(3))

    def jugar_partida_mitjana():
        root.destroy()
        root.after(100, lambda: pong.jugar_pong(3))

    def jugar_partida_llarga():
        root.destroy()
        root.after(100, lambda: pong.jugar_pong(3))

    btn_font = ("Courier", 16, "bold")
    btn_bg = "white"
    btn_fg = "black"
    btn_active_bg = "grey"


    # Crear botons
    # Botons de selecció de partida
    tk.Button(root, text="Partida curta (3 punts)", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=25, height=2, command=jugar_partida_curta).pack(pady=10)

    tk.Button(root, text="Partida mitjana (6 punts)", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=25, height=2, command=jugar_partida_mitjana).pack(pady=10)

    tk.Button(root, text="Partida llarga (9 punts)", font=btn_font,
              bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
              width=25, height=2, command=jugar_partida_llarga).pack(pady=10)



    # Això ha d'estar al final
    root.mainloop()

crear_menu()

