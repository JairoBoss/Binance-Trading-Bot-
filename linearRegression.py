import numpy as np
import matplotlib.pyplot as plt
import config
from binance.client import Client
from binance.enums import *
import openpyxl as xl

client = Client(config.API_KEY, config.API_SECRET, tld='com')
symbolTicker = 'YFIIUSDT'

klines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERVAL_1MINUTE, "3 day ago UTC")

precios = []
numeros = []


for i in range (1,4320):
    precios.append(float(klines[i][4]))
            
preciosArray = np.array(precios)
aa = 0
for i in (precios):
    numeros.append(aa+1)
    aa = aa+1
    
numerosArray = np.array(numeros)

print(preciosArray)





def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

def main():
	# observations / data
	x = np.array(numeros)
	y = np.array(precios)
 
# ? 33566.44000000
	# estimating coefficients
	b = estimate_coef(x, y)
	print("Estimated coefficients:\nb_0 = {} \
		\nb_1 = {}".format(b[0], b[1]))

	# plotting regression line
	plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()
