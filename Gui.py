import tkinter as tk
import time
from PIL import Image, ImageTk
#245 280
class A:
    def __init__(self, master):
        
        

        self.img = Image.open("Grafica.png")
        self.img = self.img.resize((470, 275))
        self.tkimage = ImageTk.PhotoImage(self.img)
        tk.Label(root, image=self.tkimage).grid()


        self.lbltiempo = tk.Label(master)
        self.lbltiempo.configure(text ='Tiempo x Minuto')
        self.lbltiempo.place(relx = .160, rely = .9033)
        self.lbltiempo.configure(bg='white')

        self.lbltiempo = tk.Label(master)
        self.lbltiempo.configure(text ='P\nR\nE\nC\nI\nO')
        self.lbltiempo.place(relx = .471, rely = .23090)
        self.lbltiempo.configure(bg='white')

        
        self.lblGanacias = tk.Label(master)
        self.lblGanacias.configure(text ='Gancias ')
        self.lblGanacias.place(relx = .560, rely = .1090)
        self.lblGanacias.configure(bg='white')

        self.lblGanaciasDinero = tk.Label(master)
        self.lblGanaciasDinero.configure(text ='Null')
        self.lblGanaciasDinero.place(relx = .560, rely = .258)
        self.lblGanaciasDinero.configure(bg='white')

        self.lblPerdida = tk.Label(master)
        self.lblPerdida.configure(text ='Perdida')
        self.lblPerdida.place(relx = .560, rely = .5272)
        self.lblPerdida.configure(bg='white')


        self.lblPerdidaDinero = tk.Label(master)
        self.lblPerdidaDinero.configure(text ='Null')
        self.lblPerdidaDinero.place(relx = .560, rely = .677)
        self.lblPerdidaDinero.configure(bg='white')

        self.lblUltimasOperacopmes = tk.Label(master)
        self.lblUltimasOperacopmes.configure(text ='Ultimas operaciones')
        self.lblUltimasOperacopmes.place(relx = .795, rely = .1090)
        self.lblUltimasOperacopmes.configure(bg='white')

        self.lblOperacionUno = tk.Label(master)
        self.lblOperacionUno.configure(text ='------------------')
        self.lblOperacionUno.place(relx = .680, rely = .258)
        self.lblOperacionUno.configure(bg='white')

        self.lblOperacionDos = tk.Label(master)
        self.lblOperacionDos.configure(text ='------------------')
        self.lblOperacionDos.place(relx = .680, rely = .403)
        self.lblOperacionDos.configure(bg='white')

        self.lblOperacionTres = tk.Label(master)
        self.lblOperacionTres.configure(text ='------------------')
        self.lblOperacionTres.place(relx = .680, rely = .548)
        self.lblOperacionTres.configure(bg='white')

        self.lblOperacionCuatro = tk.Label(master)
        self.lblOperacionCuatro.configure(text ='------------------')
        self.lblOperacionCuatro.place(relx = .680, rely = .7096)
        self.lblOperacionCuatro.configure(bg='white')
       #710 80 


        self.count = 0
        self.update_label()

    def update_label(self):
        if self.count < 10000:
            #############################
            #############################
            #############################
            #Aqui solo pon tu funcion de ganancia y perdida
            self.lblGanaciasDinero.configure(text = '+ $ {} USDT'.format(self.count))
            self.lblGanaciasDinero.after(10000, self.update_label) 

            self.ayuda = 0
            self.lblPerdidaDinero.configure(text = '- $ {} USDT'.format(self.ayuda))
            self.lblPerdidaDinero.after(1000, self.update_label) 

            #############################
            #############################
            #############################
            #Aqui pasele el string del detalle de las operaciones

            self.lblOperacionUno.configure(text = 'Sab 22 Mayo Se vendio a 58,634 gano $20 USDT ')
            #self.lblOperacionUno.after(1000, self.update_label) 

            self.lblOperacionDos.configure(text = '------------------')
            #self.lblOperacionDos.after(1000, self.update_label) 
            
            self.lblOperacionTres.configure(text = '------------------')
            #self.lblOperacionTres.after(1000, self.update_label) 

            self.lblOperacionCuatro.configure(text = '------------------')
            #self.lblOperacionCuatro.after(1000, self.update_label)

            



            self.count += 1
        #print self.count


root = tk.Tk(className='Binance Trading bot')
root.geometry("1000x310")
root.configure(bg='white')
A(root)
root.mainloop()
