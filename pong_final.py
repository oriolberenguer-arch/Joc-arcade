import tkinter as tk
import pong
import menu_pong
import pygame

pygame.init()


def pantalla_final(guanyador, puntuacio_max):
    root = tk.Tk()
    root.title("Jugador guanyador")
    root.attributes('-fullscreen', True)
    root.configure(bg="black") 


    def reiniciar():
        root.destroy()
        pong.jugar_pong(puntuacio_max)

    def tornar_menu():
        root.destroy()
        menu_pong.crear_menu()


    cartell = tk.Label(root, text=f"JUGADOR {guanyador} GUANYADOR", font=("Courier", 72, "normal"), fg="white", bg="black")
    cartell.pack(pady=75)


    boto_reiniciar = tk.Button(root, text="Reiniciar", font=("Courier", 36, "normal"), fg="black", bg="white", activebackground="grey",
                               command=reiniciar)
    boto_menu = tk.Button(root, text="Tornar al menú", font=("Courier", 36, "normal"), fg="black", bg="white", activebackground="grey",
                          command=tornar_menu)
    boto_reiniciar.pack()
    boto_menu.pack()


    root.mainloop()

