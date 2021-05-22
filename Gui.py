import tkinter as tk


#Ventana raiz Java equivalente al JFrame
root = tk.Tk()

#Creando el Label, equivalente al JLabel

lblGanacias = tk.Label(root, text ='Ganancias')
lblPerdida = tk.Label(root, text ='Perdida')
#Esto es para poner la posicion
lblGanacias.place(relx = .1, rely = .1)
lblPerdida.place(relx = .3, rely = .3)
# Poner visible Frame, equivalente al .setVisible(true)
root.mainloop()
