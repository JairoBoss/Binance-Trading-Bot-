import tkinter as tk
import time
from PIL import Image, ImageTk
import threading
import config
import func
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np
import winsound as ws
import matplotlib.pyplot as plt


client = Client(config.API_KEY, config.SECRET, tld='com')
symbolTicker = 'BNBUSDT'
precioCompra = 0
quantityOrders = 0
compra = False
ganancia = 0
inversion = 1000
porcentaje_comision = .00075


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
        
        self.img = Image.open("grafica.png")
        self.img = self.img.resize((470, 275))
        self.tkimage = ImageTk.PhotoImage(self.img)
        self.lblImg = tk.Label(root, image=self.tkimage).grid()    

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
            list_of_tickers = client.get_all_tickers()
            for tick_2 in list_of_tickers:
                if tick_2["symbol"] == symbolTicker:
                    precioCompra = float(tick_2["price"])

            if ((precioCompra >= max*.991) and ((precioCompra >= ((media_max+max)/2)*.991))): 
                ws.MessageBeep(type=1)

                list_of_tickers = client.get_all_tickers()
                for tick_2 in list_of_tickers:
                    if tick_2["symbol"] == symbolTicker:
                        precioActual = float(tick_2["price"])

                comisionCompra = (inversion*porcentaje_comision)
                comisionVenta = (inversion+((precioActual-precioCompra) /precioActual))*porcentaje_comision

                gananciaTR = ((precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta)

                if (((comisionCompra+comisionVenta) < ((precioActual - precioCompra)*(inversion/precioCompra))) or (gananciaTR <= (-inversion*.02))):
                    ws.MessageBeep(type=1)
                    
                    ganancia += (precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta
                    
                    texto = ('Se vendió a: ', precioActual, ' ganó: ', gananciaTR) 
                
                
                    



            self.lblGanaciasDinero.configure(text = gananciaTR) 
            self.lblGanaciasDinero.after(2500, self.update_label)             
        
            self.lblPerdidaDinero.configure(text = precioCompra)
            #self.lblPerdidaDinero.after(5000, self.update_label) 

            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
            precio = [float(klines[len(klines)-1][2]),float(klines[len(klines)-2][2]),float(klines[len(klines)-3][2]),float(klines[len(klines)-4][2]),float(klines[len(klines)-5][2]), float(klines[len(klines)-6][2]), float(klines[len(klines)-7][2]), float(klines[len(klines)-8][2]), float(klines[len(klines)-9][2]), float(klines[len(klines)-10][2])]
            tiempo = [10,9,8,7,6,5,4,3,2,1]
            
            plt.plot(tiempo, precio)
            plt.title('Precio Vs tiempo')
            plt.xlabel('Tiempo')
            plt.ylabel('Precio')
            plt.savefig('grafica.png')
                
            self.lblImg

            #############################
            #############################
            #############################
            #Aqui pasele el string del detalle de las operaciones

            self.lblOperacionUno.configure(text = 'Se vendió a 270.898, ganó: 0.277806790')
            #self.lblOperacionUno.after(5000, self.update_label) 
            if(texto == ''):
                print("")
            else:
                self.lblOperacionDos.configure(text = texto)
            #self.lblOperacionDos.after(1000, self.update_label) 
            
            self.lblOperacionTres.configure(text = '------------------')
            #self.lblOperacionTres.after(1000, self.update_label) 

            self.lblOperacionCuatro.configure(text = '------------------')
            #self.lblOperacionCuatro.after(1000, self.update_label)

            self.count += 1


root = tk.Tk(className='Binance Trading bot')
root.geometry("1000x310")
root.configure(bg='white')
A(root)     

root.mainloop()



    




    
    

