import os 
import matplotlib.pyplot as plt
import numpy as np

start = len("HEADER    IMMUNE SYSTEM                           13-NOV-")
stop = start + 3

proteins = os.listdir('proteins/')

date = []

for i, protein in enumerate(proteins): 
	f = open("proteins/" + protein, 'r')
	num = int(f.read().split("\n")[0][start: stop])

	if num > 80: num += 1900
	else: num += 2000

	date.append(num)
	print("[%i / %i] %s"%(i+1, len(proteins), date[-1]))
	

first_year 	= np.min(date)
last_year 	= np.max(date)
bins 		= np.bincount(date)[first_year: last_year+1]
plt.plot(range(first_year, last_year+1), bins, 'x')
plt.ylabel("# Proteins Scanned")
plt.xlabel("Year")
plt.show()
