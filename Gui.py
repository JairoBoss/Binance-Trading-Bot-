import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


#Ventana raiz Java equivalente al JFrame
root = tk.Tk(className='Binance Trading bot')
root.geometry("1000x310")

#img = Image.open("Grafica.png")
#img = img.resize((470, 275))
#795 30
#
#tkimage = ImageTk.PhotoImage(img)
#tk.Label(root, image=tkimage).grid()

var = StringVar()
var.set('GANANCIASSSSSSSSSSS')

#Creando el Label, equivalente al JLabel

lblGanacias = tk.Label(root, text =var)

lblPerdida = tk.Label(root, text ='Perdida')

lblUltimasOperacopmes = tk.Label(root, text ='Ultimas operaciones')
#Esto es para poner la posicion
lblGanacias.place(relx = .560, rely = .1090)
lblPerdida.place(relx = .560, rely = .5272)
lblUltimasOperacopmes.place(relx = .795, rely = .1090)



root.mainloop()

    

# Poner visible Frame, equivalente al .setVisible(true)


