import numpy as np

def media_max_klines(klines):
    suma = 0
    for i in range(len(klines)):
        suma = suma + float(klines[i][2])  
    media = suma / len(klines)
    return media

def media_min_klines(klines):
    suma = 0  
    for i in range(len(klines)):
        suma = suma + float(klines[i][3])  
    media = suma / len(klines)
    return media