import os 
import matplotlib.pyplot as plt
import numpy as np

start = len("HEADER    IMMUNE SYSTEM                           13-NOV-")
stop = start + 3

proteins = os.listdir('proteins/')

date 		= []
temperature = []
ph 			= []

res_high 	= []
res_low 	= []
res_compl	= []
refl_count	= []

protein_atoms = []

for i, protein in enumerate(proteins): 
	f = open("proteins/" + protein, 'r')
	lines = f.read().split("\n")
	num = int(lines[0][start: stop])
	
	for j, line in enumerate(lines): 
		if "TEMPERATURE           (KELVIN)" in line: 
			temperature_place = "".join(list(line.split(":")[1])[1:4]) # can be NUL
			if temperature_place != "NUL": 
				temperature.append(int(temperature_place))

		if "PH                             : " in line: 
			ph_place = "".join(list(line.split(":")[1])[1:4]) # can be NUL
			if ph_place != "NUL" and ph_place != "APP":  # NULL or APPROX, not sure what last means. 
				ph.append(float(ph_place))

	
		if "RESOLUTION RANGE HIGH (ANGSTROMS) : " in line: 
			place = "".join(list(line.split(" :")[1])[1:5])
			res_low.append(float(place))

		if "RESOLUTION RANGE LOW  (ANGSTROMS) : " in line: 
			place = "".join(list(line.split(" :")[1])[1:5])
			if place != "NULL": 
				res_high.append(float(place))

		if "REMARK   3   COMPLETENESS FOR RANGE        (%) : " in line: 
			place = "".join(list(line.split(" :")[1])[1:5])
			if place != "NULL": 
				res_compl.append(int(float(place)))
		
		if "REMARK   3   NUMBER OF REFLECTIONS             : " in line: 
			place = "".join(list(line.split(" :")[1])[1:5])
			if place != "NULL": 
				refl_count.append(int(place))

		if "REMARK   3   PROTEIN ATOMS            : " in line: 
			place = "".join(list(line.split(" :")[1])[1:7])
			if place != "NULL  ": 
				protein_atoms.append(int(place))



	if num > 80: num += 1900
	else: num += 2000

	date.append(num)
	print("[%i / %i] %s"%(i+1, len(proteins), date[-1]))
	

fig, ax = plt.subplots(4, 4, figsize=(10, 10))

num = len(proteins)
bins = 100

#x, y = histogramify(date)
ax[0,0].hist(date, bins=bins)#(np.max(date)-np.min(date)))
ax[0,0].set_ylabel("# Proteins ")
ax[0,0].set_xlabel("Year")
ax[0,0].set_title("%i / %i = %.3f"%(len(date), num, len(date)/num))

ax[0,1].hist(temperature, bins=bins)#(np.max(temperature) - np.min(temperature)))
ax[0,1].set_xlabel("Temperature [K]")
ax[0,1].set_title("%i / %i = %.3f"%(len(temperature), num, len(temperature)/num))

ax[0,2].hist(ph, bins=bins)#int(np.max(ph)*10 - np.min(ph)*10))
ax[0,2].set_xlabel("Temperature [K]")
ax[0,2].set_title("%i / %i = %.3f"%(len(ph), num, len(ph)/num))


ax[0,3].hist(protein_atoms, bins=bins)#(len(protein_atoms)))
ax[0,3].set_title("%i / %i = %.3f"%(len(protein_atoms), num, len(protein_atoms)/num))
ax[0,3].set_xlabel("Protein Atoms")

# resolution and reflctions
ax[1,0].hist(res_low, bins=bins)#int(np.max(res_low)*10-np.min(res_low)*10))
ax[1,0].set_title("%i / %i = %.3f"%(len(res_low), num, len(res_low)/num))
ax[1,0].set_xlabel("Resolution Low [Å]")


ax[1,1].hist(res_high, bins=bins)#int(np.max(res_high)*10-np.min(res_high)*10))
ax[1,1].set_title("%i / %i = %.3f"%(len(res_high), num, len(res_high)/num))
ax[1,1].set_xlabel("Resolution High [Å]")


ax[1,2].hist(res_compl, bins=bins)#int(np.max(res_compl)-np.min(res_compl)))
ax[1,2].set_title("%i / %i = %.3f"%(len(res_compl), num, len(res_compl)/num))
ax[1,2].set_xlabel("Resolution Completeness")


ax[1,3].hist(refl_count, bins=bins)#(np.max(refl_count)-np.min(refl_count)))
ax[1,3].set_title("%i / %i = %.3f"%(len(refl_count), num, len(refl_count)/num))
ax[1,3].set_xlabel("Reflection Count")




plt.tight_layout()
plt.show()
