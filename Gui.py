import tkinter as tk
from tkinter import *
import time
from tkinter.constants import X
from PIL import Image, ImageTk
import threading
import config
import func
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np
#import winsound as ws
import matplotlib.pyplot as plt


client = Client(config.API_KEY, config.API_SECRET, tld='com')
symbolTicker = 'BNBUSDT'
precioCompra = 0
quantityOrders = 0
compra = False
ganancia = 0
inversion = 1000
porcentaje_comision = .00075

root = tk.Tk(className='Binance Trading bot')
root.geometry("0x0")

def userIncorrect():
    top = Toplevel()
    top.title("Usuario incorrecto")
    top.geometry("200x50")
    l2 = Label(top, text = "Porfavor ingresa un usuario correcto")
    l2.pack()
    

def x():    
    root.geometry("1000x310")
    root.configure(bg='white')
    root1.destroy()

    A(root)  
    root.mainloop()    
    

#245 280
class A:
    
    def __init__(self, master):
        klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
        precio = [float(klines[len(klines)-1][2]),float(klines[len(klines)-2][2]),float(klines[len(klines)-3][2]),float(klines[len(klines)-4][2]),float(klines[len(klines)-5][2]), float(klines[len(klines)-6][2]), float(klines[len(klines)-7][2]), float(klines[len(klines)-8][2]), float(klines[len(klines)-9][2]), float(klines[len(klines)-10][2])]
        tiempo = [10,9,8,7,6,5,4,3,2,1]
        
        plt.plot(tiempo, precio)
        plt.title('Precio Vs tiempo')
        plt.xlabel('Tiempo')
        plt.ylabel('Precio')
        plt.savefig('grafica.png')

        self.precioCompra = 0
        
        self.img = Image.open("grafica.png")
        self.img = self.img.resize((470, 275))
        self.tkimage = ImageTk.PhotoImage(self.img)
        self.lblImg = tk.Label(root)
        self.lblImg.configure(image=self.tkimage)
        self.lblImg.grid()      

        self.lbltiempo = tk.Label(master)
        self.lbltiempo.configure(text ='Tiempo x Minuto')
        self.lbltiempo.place(relx = .160, rely = .9033)
        self.lbltiempo.configure(bg='white')

        self.lbltiempo = tk.Label(master)
        self.lbltiempo.configure(text ='P\nR\nE\nC\nI\nO')
        self.lbltiempo.place(relx = .471, rely = .23090)
        self.lbltiempo.configure(bg='white')

        self.lblGanacias = tk.Label(master)
        self.lblGanacias.configure(text ='Ganancias ')
        self.lblGanacias.place(relx = .560, rely = .1090)
        self.lblGanacias.configure(bg='white')

        self.lblGanaciasDinero = tk.Label(master)
        self.lblGanaciasDinero.configure(text ='Null')
        self.lblGanaciasDinero.place(relx = .560, rely = .258)
        self.lblGanaciasDinero.configure(bg='white')

        self.lblPerdida = tk.Label(master)
        self.lblPerdida.configure(text ='Precio actual')
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
        texto = ''
        if self.count < 10000:
            gananciaTR = 0
            ganancia = 0
            #############################
            #############################
            #############################
            #Aqui solo pon tu funcion de ganancia y perdida      
            

            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
            klines_h = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)

            min = func.min(klines)
            max = func.max(klines)

            media_min = func.media_min_klines(klines_h)
            media_max = func.media_max_klines(klines_h)                        

            # Encontrar el valor de la moneda
            if(self.precioCompra == 0):
                list_of_tickers = client.get_all_tickers()
                for tick_2 in list_of_tickers:
                    if tick_2["symbol"] == symbolTicker:
                        self.precioCompra = float(tick_2["price"])            

            if ((self.precioCompra >= max*.991) and ((self.precioCompra >= ((media_max+max)/2)*.991))): 
                #.MessageBeep(type=1)

                list_of_tickers = client.get_all_tickers()
                for tick_2 in list_of_tickers:
                    if tick_2["symbol"] == symbolTicker:
                        precioActual = float(tick_2["price"])      

                self.lblPerdidaDinero.configure(text = round(precioActual,3))                                             

                comisionCompra = (inversion*porcentaje_comision)
                comisionVenta = (inversion+((precioActual-self.precioCompra) /precioActual))*porcentaje_comision

                gananciaTR = ((precioActual - self.precioCompra)*(inversion / self.precioCompra)-comisionCompra-comisionVenta)

                if (((comisionCompra+comisionVenta) < ((precioActual - self.precioCompra)*(inversion/self.precioCompra))) or (gananciaTR <= (-inversion*.02))):
                    #ws.MessageBeep(type=1)
                    
                    ganancia += (precioActual - self.precioCompra)*(inversion / self.precioCompra)-comisionCompra-comisionVenta
                    
                    texto = ('Se vendi?? a: ', precioActual, ' gan??: ', gananciaTR)      
                    self.precioCompra= 0                        

            self.lblGanaciasDinero.configure(text = gananciaTR) 
            self.lblGanaciasDinero.after(2500, self.update_label)                                 
            

            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
            precio = [float(klines[len(klines)-1][2]),float(klines[len(klines)-2][2]),float(klines[len(klines)-3][2]),float(klines[len(klines)-4][2]),float(klines[len(klines)-5][2]), float(klines[len(klines)-6][2]), float(klines[len(klines)-7][2]), float(klines[len(klines)-8][2]), float(klines[len(klines)-9][2]), float(klines[len(klines)-10][2])]
            tiempo = [10,9,8,7,6,5,4,3,2,1]
            
            plt.clf()
            plt.plot(tiempo, precio)
            plt.title('Precio Vs tiempo')
            plt.xlabel('Tiempo')
            plt.ylabel('Precio')
            plt.savefig('grafica.png')

            self.img2 = Image.open("grafica.png")
            self.img2 = self.img2.resize((470, 275))
            self.tkimage = ImageTk.PhotoImage(self.img2)
            self.lblImg.configure(image=self.tkimage)

            #############################
            #############################
            #############################
            #Aqui pasele el string del detalle de las operaciones

            self.lblOperacionUno.configure(text = 'Se vendi?? a 270.898, gan??: 0.277806790')
            #self.lblOperacionUno.after(5000, self.update_label)            
            self.lblOperacionDos.configure(text = texto)
            #self.lblOperacionDos.after(1000, self.update_label) 
            
            

            self.lblOperacionTres.configure(text = '------------------')
            #self.lblOperacionTres.after(1000, self.update_label) 

            self.lblOperacionCuatro.configure(text = '------------------')
            #self.lblOperacionCuatro.after(1000, self.update_label)

            self.count += 1

root1 = tk.Tk(className='Login')
root1.geometry("1000x310")


lblInicio = tk.Label(root1, text="Ingresa tus credenciales").pack()

usuarioString = StringVar()
passwordString = StringVar()

lblLogin = tk.Label(root1, text="Usuario : ").pack()

username_login_entry = Entry(root1, textvariable=usuarioString)
username_login_entry.pack()

lblPassword = tk.Label(root1, text="Contrase??a : ").pack()

password_login_entry = Entry(root1, textvariable=passwordString, show= '*')
password_login_entry.pack()

   

botoncito = tk.Button(root1, text="Login", command=x).pack()
root1.mainloop()


###
usdt = 29.28406905
comision = round((usdt * .001),8)
total = 29.29 - comision
print(f"La comision es de: {comision}")
print(f"El total es: {total}")
###
