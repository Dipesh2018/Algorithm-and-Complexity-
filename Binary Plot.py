#plotting graph for binary search

from time import time
import matplotlib.pyplot as plt 
import random
from binary_search import binary_Search,split

def main():
	number = 5
	x_cord,y_cord = [],[]
	b=1
	for i in range(0,5):
		b = b * 10
		data = random.sample(range(b),b)
		start = time()	
		binary_Search(data,number)
		final = time()
		elapsed = final - start
		x_cord.append(b)
		y_cord.append(elapsed)
	plt.plot(x_cord,y_cord)
	plt.show()

main()
