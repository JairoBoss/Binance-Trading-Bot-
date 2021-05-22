import numpy as np

def media_max_klines(klines):
    suma = 0     
    for i in range(10):        
        suma = suma + float(klines[len(klines)-(i+1)][2])  
    media = suma / 10
    return media

def media_min_klines(klines):
    suma = 0     
    for i in range(10):        
        suma = suma + float(klines[len(klines)-(i+1)][3])  
    media = suma / 10
    return media

def min(klines):
    min = 0
    for i in range(10):
        piv = float(klines[len(klines)-(i+1)][3])
        if ((piv <= min) or (min == 0)):
            min = piv
    return min
    
def max(klines):
    max = 0
    for i in range(10):
        piv = float(klines[len(klines)-(i+1)][2])
        if ((piv >= max) or (max == 0)):
            max = piv
    return max