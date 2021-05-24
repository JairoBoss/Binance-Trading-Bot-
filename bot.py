import config
import func
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np
import winsound as ws
import matplotlib.pyplot as plt
import threading

class myThread (threading.Thread):
    def __init__(self, valores):
        gananciaTR = 0
        texto = ""

    def run(self):
        client = Client(config.API_KEY, config.SECRET, tld='com')
        symbolTicker = 'BNBUSDT'
        precioCompra = 0
        quantityOrders = 0
        compra = False
        ganancia = 0
        inversion = 1000
        porcentaje_comision = .00075

        while 1:

            time.sleep(1)

            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
            klines_h = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)

            min = func.min(klines)
            max = func.max(klines)

            media_min = func.media_min_klines(klines_h)
            media_max = func.media_max_klines(klines_h)

            
            precio = [float(klines[len(klines)-1][2]),float(klines[len(klines)-2][2]),float(klines[len(klines)-3][2]),float(klines[len(klines)-4][2]),float(klines[len(klines)-5][2]), float(klines[len(klines)-6][2]), float(klines[len(klines)-7][2]), float(klines[len(klines)-8][2]), float(klines[len(klines)-9][2]), float(klines[len(klines)-10][2])]
            tiempo = [10,9,8,7,6,5,4,3,2,1]
            
            plt.plot(tiempo, precio)
            plt.title('Precio Vs tiempo')
            plt.xlabel('Tiempo')
            plt.ylabel('Precio')

            # Encontrar el valor de la moneda
            list_of_tickers = client.get_all_tickers()
            for tick_2 in list_of_tickers:
                if tick_2["symbol"] == symbolTicker:
                    precioCompra = float(tick_2["price"])

            if ((precioCompra >= max*.991) and ((precioCompra >= ((media_max+max)/2)*.991))): 
                '(precioCompra <= ((media_min+min)/2)*1.007) or '
                'or ((precioCompra <= (float(klines[len(klines)-1][3]))) + (float(klines[len(klines)-1][3])*.01)'
                ws.MessageBeep(type=1)
                print("*** Compra inicial ***")
                print("Se compro a: ", precioCompra)
                # order = client.order_market_buy(
                #    symbol = symbolTicker,
                #   quantity = quantityOrders
                # )   
                break              
            else:
                print("\nPrecio actual",precioCompra)
                print("\nPrecio máximo de 1hr min",max)
                print("\nPrecio mínimo de 1hr min",min)
                print("\nMedia de precio máximo de 30 mins", media_max)
                print("\nMedia de precio mínimo de 30 mins", media_min)        
                print("\nEsa wea max", ((media_max+max)/2)*.993)
                print("\nEsa wea min", ((media_min+min)/2)*1.007)
                print("\nbuscando precio..")

        while 1:
            time.sleep(1)
            # Encontrar el valor de la moneda
            list_of_tickers = client.get_all_tickers()
            for tick_2 in list_of_tickers:
                if tick_2["symbol"] == symbolTicker:
                    precioActual = float(tick_2["price"])

            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_5MINUTE)        

            

            comisionCompra = (inversion*porcentaje_comision)
            comisionVenta = (inversion+((precioActual-precioCompra) /precioActual))*porcentaje_comision

            print("***********")
            print("Se desea comprar a: ", (precioCompra+comisionCompra+comisionVenta))

            gananciaTR = ((precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta)

            print("Ganancia tiempo real:", gananciaTR)        

            if (((comisionCompra+comisionVenta) < ((precioActual - precioCompra)*(inversion/precioCompra))) or (gananciaTR <= (-inversion*.02))):
                print("Se vendio a: ", precioActual)
                ws.MessageBeep(type=1)

                texto = ("Se vendió a: ", precioActual, " ganó: ", ganancia)

                ganancia += (precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta
                    # order = client.order_market_sell(
                    #    symbol = symbolTicker,
                    #    quantity = 0.00022
                    # )
                compra = True
                precioCompra = precioActual

                time.sleep(2)

                while 1:
                    klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE) 
                    
                    klines_h = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)

                    min = func.min(klines)
                    max = func.max(klines)

                    media_min = func.media_min_klines(klines_h)
                    media_max = func.media_max_klines(klines_h)

                    list_of_tickers = client.get_all_tickers()
                    for tick_2 in list_of_tickers:
                        if tick_2["symbol"] == symbolTicker:
                            precioCompra = float(tick_2["price"])

                    print("\nPrecio actual",precioCompra)
                    print("\nPrecio máximo de 1hr min",max)
                    print("\nPrecio mínimo de 1hr min",min)
                    print("\nMedia de precio máximo de 1 hr", media_max)
                    print("\nMedia de precio mínimo de 1 hr", media_min)        
                    print("\nEsa wea max", ((media_max+max)/2)*.993)
                    print("\nEsa wea min", ((media_min+min)/2)*1.007)
                    print("\nbuscando precio..")

                    if ((precioCompra >= max*.991) and ( (precioCompra >= ((media_max+max)/2)*.991))):
                        print("Se compra a: ", precioCompra)
                        ws.MessageBeep(type=1)
                        # order = client.order_market_buy(
                        #symbol = symbolTicker,
                        #quantity = quantityOrders
                        # )

                        break

                    time.sleep(1)

            else:
                print("El precio es menor, paso")
                print("El precio al que se compro es: ", precioCompra)
                print("La suma de comisiones es: ", (comisionCompra+comisionVenta))
                print("El precio es de: ", precioActual)
                print("Ganancia: ", ganancia)

    


