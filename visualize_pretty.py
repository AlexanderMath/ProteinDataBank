import pickle
import os 
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

proteins = os.listdir('proteins/')

fig, ax = plt.subplots(1, 1, figsize=(8, 3))

num  = len(proteins)
bins = 100

with open ('lists.pckl', 'rb') as fp:
    lst = pickle.load(fp)

date = lst[0] 	
temperature = lst[1]
ph 			= lst[2]
res_high 	= lst[3]
res_low 	= lst[4] 
res_compl	= lst[5]
refl_count	= lst[6]
protein_atoms  = lst[7]

date = np.sort(date)
print(date)
unique, counts = np.unique(date, return_counts=True)
d = dict(zip(unique, counts))
print(d)

ax.plot(unique, np.cumsum(counts))
ax.set_ylabel("Total Number of Proteins. ")
ax.set_xlabel("Year. ")
ax.set_yscale("log")
ax.set_title("Number of Human Proteins in wwPDB from 1986 to 2017. ")
ax.set_xlim([1986, 2017])
ax.set_ylim([10, 10**5])

plt.tight_layout()
plt.savefig("pretty.pdf")
plt.show()
