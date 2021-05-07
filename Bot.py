import config
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np

client = Client(config.API_KEY, config.API_SECRET, tld='com')
symbolTicker = 'BTCUSDT'
precioAnterior = 0
quantityOrders = 400
compra = False
ganancia = 0


#Encontrar el valor de la moneda
list_of_tickers = client.get_all_tickers()
for tick_2 in list_of_tickers:
    if tick_2["symbol"] == symbolTicker:
        precioAnterior = float(tick_2["price"])

print ("*** Compra inicial ***")
print("Se compro a: ", precioAnterior)
order = client.order_market_buy(
    symbol = symbolTicker,
    quantity = quantityOrders
)


while 1:
    time.sleep(3)
    #Encontrar el valor de la moneda
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            precioActual = float(tick_2["price"])

    print("***********")
    #print("Se desea comprar a: ", (precioAnterior+(precioAnterior*.001)))    
    if ((precioAnterior+(precioAnterior*.001)) < (precioActual)):
        print("Se vendio a: ", precioActual) 
        ganancia += ((precioActual - (precioAnterior-(precioAnterior*.001)))*(1000/precioAnterior))
        order = client.order_market_sell(
            symbol = symbolTicker,
            quantity = 0.00022
        )
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
            
            if (precioActual < ((precioActual*.001)+precioActual)):
                print("Se compra a: ", precioActual)
                order = client.order_market_buy(
                symbol = symbolTicker,
                quantity = quantityOrders
                )
                
                break

            #time.sleep(3)
                

    else:
        print("El precio es menor, paso")
        print("El precio es de: ", precioActual)
        print("Ganancia: ", ganancia)
        
