import tkinter as tk
import pong_ai
import menu_pong


def pantalla_final(guanyador, puntuacio_max):
    root = tk.Tk()
    root.title("Jugador guanyador")
    root.geometry("800x600")
    root.configure(bg="black") 


    def reiniciar():
        root.destroy()
        pong_ai.jugar_pong(puntuacio_max)

    def tornar_menu():
        root.destroy()
        menu_pong.crear_menu()


    cartell = tk.Label(root, text=f"JUGADOR {guanyador} GUANYADOR", font=("Courier", 48, "normal"), fg="white", bg="black")
    cartell.pack(pady=50)


    boto_reiniciar = tk.Button(root, text="Reiniciar", font=("Courier", 24, "normal"), fg="black", bg="white", activebackground="grey",
                               command=reiniciar)
    boto_menu = tk.Button(root, text="Tornar al menú", font=("Courier", 24, "normal"), fg="black", bg="white", activebackground="grey",
                          command=tornar_menu)
    boto_reiniciar.pack()
    boto_menu.pack()


    root.mainloop()

