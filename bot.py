import config
import func
from binance.client import Client
from binance.enums import *
import time
import datetime
import numpy as np

client = Client(config.API_KEY, config.SECRET, tld='com')
symbolTicker = 'BNBUSDT'
precioCompra = 0
quantityOrders = 0
compra = False
ganancia = 0
inversion = 1000
porcentaje_comision = .00075



while 1:
    klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_5MINUTE)
    klines_h = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)

    media_min = func.media_min_klines(klines_h)

    # Encontrar el valor de la moneda
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            precioCompra = float(tick_2["price"])

    if ((precioCompra <= float(klines[len(klines)-1][3]) and (precioCompra <= media_min))):  
        'or ((precioCompra <= (float(klines[len(klines)-1][3]))) + (float(klines[len(klines)-1][3])*.01)'
        print("*** Compra inicial ***")
        print("Se compro a: ", precioCompra)
        # order = client.order_market_buy(
        #    symbol = symbolTicker,
        #   quantity = quantityOrders
        # )
        break
    else:
        print("\nPrecio actual",precioCompra)
        print("\nPrecio mínimo de 5 min",float(klines[len(klines)-1][3]))
        print("\nMedia de precio mínimo de 30 mins", media_min)
        print("\nbuscando precio..")

while 1:
    time.sleep(3)
    # Encontrar el valor de la moneda
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            precioActual = float(tick_2["price"])

    klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_5MINUTE)        

    maximo = klines[len(klines)-1][2]
    minimo = klines[len(klines)-1][3]

    print("Máximo: ", maximo)
    print("Mínimo: ", minimo)

    comisionCompra = (inversion*porcentaje_comision)
    comisionVenta = (inversion+((precioActual-precioCompra) /precioActual))*porcentaje_comision

    print("***********")
    print("Se desea comprar a: ", (precioCompra+comisionCompra+comisionVenta))

    gananciaTR = ((precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta)

    print("Ganancia tiempo real:", gananciaTR)

    if (((comisionCompra+comisionVenta) < ((precioActual - precioCompra)*(inversion/precioCompra)))):
        print("Se vendio a: ", precioActual)
        ganancia += (precioActual - precioCompra)*(inversion / precioCompra)-comisionCompra-comisionVenta
        # order = client.order_market_sell(
        #    symbol = symbolTicker,
        #    quantity = 0.00022
        # )
        print("Ganancia: ", ganancia)
        compra = True
        precioCompra = precioActual

        time.sleep(15)

        while 1:
            klines = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_5MINUTE) 

            
            klines_h = client.get_klines(symbol=symbolTicker, interval=Client.KLINE_INTERVAL_1MINUTE)
    
            media_min = func.media_min_klines(klines_h)

            list_of_tickers = client.get_all_tickers()
            for tick_2 in list_of_tickers:
                if tick_2["symbol"] == symbolTicker:
                    precioCompra = float(tick_2["price"])

            print("\nPrecio actual",precioCompra)
            print("\nPrecio mínimo de 5 min",float(klines[len(klines)-1][3]))
            print("\nMedia de precio mínimo de 30 mins", media_min)
            print("\nbuscando precio..")  

            if ((precioCompra <= float(klines[len(klines)-1][3]) and (precioCompra <= media_min))):
                print("Se compra a: ", precioCompra)
                # order = client.order_market_buy(
                #symbol = symbolTicker,
                #quantity = quantityOrders
                # )

                break

            # time.sleep(3)

    else:
        print("El precio es menor, paso")
        print("El precio al que se compro es: ", precioCompra)
        print("La suma de comisiones es: ", (comisionCompra+comisionVenta))
        print("El precio es de: ", precioActual)
        print("Ganancia: ", ganancia)
