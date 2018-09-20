import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = open("5wa1.pdb", "r")
raw = f.read()
lines = raw.split("\n")

before_part = "ATOM   1932  CG  HIS A 249     "
part = "-40.116   6.006   2.804"

# find first occurence of atom and last one
atoms = []
for i, line in enumerate(lines): 
	if "ATOM" == "".join(list(line)[:4]): 
		line = "".join(list(line)[len(before_part): len(before_part) + len(part)]).split(" ")
		nums = [float(f) for f in line if f != ""]
		atoms.append(nums)

atoms = np.array(atoms)
print(atoms.shape)
# add amino acid colors. 


fig = plt.figure()
ax = Axes3D(fig)

ax.plot(atoms[:, 0], atoms[:, 1], atoms[:, 2])
ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], 'o')
plt.show()


	

