import config
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np

client = Client(config.API_KEY, config.SECRET, tld='com')
symbolTicker = 'BNBUSDT'
precioAnterior = 0
quantityOrders = 0
compra = False
ganancia = 0
inversion = 1000
porcentaje_comision = .00075

#Encontrar el valor de la moneda
list_of_tickers = client.get_all_tickers()
for tick_2 in list_of_tickers:
    if tick_2["symbol"] == symbolTicker:
        precioAnterior = float(tick_2["price"])

print ("*** Compra inicial ***")
print("Se compro a: ", precioAnterior)
#order = client.order_market_buy(
#    symbol = symbolTicker,
 #   quantity = quantityOrders
#)

while 1:
    time.sleep(3)
    #Encontrar el valor de la moneda
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            precioActual = float(tick_2["price"])

    klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)       

    print("Máximo: ", klines[len(klines)-1][2])
    print("Mínimo: ", klines[len(klines)-1][3])

    comisionCompra = (inversion*porcentaje_comision)
    comisionVenta = (inversion+((precioActual-precioAnterior)/precioActual))*porcentaje_comision

    print("***********")
    print("Se desea comprar a: ", (precioAnterior+comisionCompra+comisionVenta))  

    gananciaTR = ((precioActual - precioAnterior)*(inversion/precioAnterior)-comisionCompra-comisionVenta)

    print("Ganancia tiempo real:", gananciaTR )
     
    if ((comisionCompra+comisionVenta)) < ((precioActual - precioAnterior)*(inversion/precioAnterior)):
        print("Se vendio a: ", precioActual) 
        ganancia += (precioActual - precioAnterior)*(inversion/precioAnterior)-comisionCompra-comisionVenta
        #order = client.order_market_sell(
        #    symbol = symbolTicker,
        #    quantity = 0.00022
        #)
        print("Ganancia: ", ganancia)
        compra = True
        precioAnterior = precioActual
        
        time.sleep(15)

        while 1:
            
            list_of_tickers = client.get_all_tickers()
            for tick_2 in list_of_tickers:
                if tick_2["symbol"] == symbolTicker:
                    precioActual = float(tick_2["price"])

            print(".---------------------------------------------------------------------.")
            print("Buscando un precio optimo para comprar, el precio actual es de:", precioActual)
            
            if (precioActual < ((precioActual*porcentaje_comision)+precioActual)):
                print("Se compra a: ", precioActual)
                #order = client.order_market_buy(
                #symbol = symbolTicker,
                #quantity = quantityOrders
                #)
                
                break

            #time.sleep(3)
                

    else:
        print("El precio es menor, paso")
        print("El precio al que se compro es: ", precioAnterior)
        print("La suma de comisiones es: ", (comisionCompra+comisionVenta))
        print("El precio es de: ", precioActual)
        print("Ganancia: ", ganancia)
