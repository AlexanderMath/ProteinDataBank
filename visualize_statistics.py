import pickle

import os 
import matplotlib.pyplot as plt
import numpy as np

proteins = os.listdir('proteins/')

fig, ax = plt.subplots(4, 4, figsize=(10, 10))

num = len(proteins)
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




#x, y = histogramify(date)
ax[0,0].hist(date, bins=bins)#(np.max(date)-np.min(date)))
ax[0,0].set_ylabel("# Proteins ")
ax[0,0].set_xlabel("Year")
ax[0,0].set_title("%i / %i = %.3f"%(len(date), num, len(date)/num))

ax[0,1].hist(temperature, bins=bins)#(np.max(temperature) - np.min(temperature)))
ax[0,1].set_xlabel("Temperature [K]")
ax[0,1].set_title("%i / %i = %.3f"%(len(temperature), num, len(temperature)/num))

ph = np.array(ph)
ax[0,2].hist(ph[ph < 15], bins=bins)#int(np.max(ph)*10 - np.min(ph)*10))
ax[0,2].set_xlabel("pH")
ax[0,2].set_title("%i / %i = %.3f"%(len(ph[ph<15]), num, len(ph[ph<15])/num))


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
