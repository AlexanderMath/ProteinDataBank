import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder

# https://rasbt.github.io/biopandas/tutorials/Working_with_PDB_Structures_in_DataFrames/
# super nice piece of code 
from biopandas.pdb import PandasPdb
import time

"""
	Input: 	Pandas PDB dataframe
	Output: One hot encoding of Amino Acid Residues and xyz position of atoms
"""
def get_axyz(pdb):
	amino_acids = pdb.df['ATOM']['residue_name']
	x = ppdb.df['ATOM']['x_coord']
	y = ppdb.df['ATOM']['y_coord']
	z = ppdb.df['ATOM']['z_coord']

	lc = LabelEncoder()
	amino_acids = lc.fit_transform(amino_acids) # one_hot encoding
	
	return amino_acids, x, y, z

# Plot protein atom by atom. 
def plot_atoms(ppdb):
	fig = plt.figure(figsize=(10, 6))
	ax_atoms 		= fig.add_subplot(1, 1, 1, projection='3d')

	amino_acids, x, y, z = get_axyz(ppdb)
	ax_atoms.scatter(x, y, z, 'o', alpha=0.3)
	plt.show()

def plot_atoms_interactive(pdb, ax_atoms):
	ax_atoms.cla()
	amino_acids, x, y, z = get_axyz(ppdb)
	ax_atoms.scatter(x, y, z, 'o', alpha=0.3)
	plt.show()

	
if __name__ == "__main__":
	save_path 	= "proteins/"
	protein_ids = ['5WA1', '5WFL', '5WFV', '5WG1'] # find more at www.rcbs.org


	plt.ion()
	fig 		= plt.figure(figsize=(10, 6))
	ax_atoms 	= fig.add_subplot(1, 1, 1, projection='3d')
	count = 0
		
	while True: 
		print("\r[%i / %i]\tCurrent Protein ID: \t%s"%(count+1, len(protein_ids), protein_ids[count]), end="")
		ppdb = PandasPdb()
		ppdb = ppdb.read_pdb(save_path + protein_ids[count] + '.pdb')
		plot_atoms_interactive(ppdb, ax_atoms)
		plt.pause(1)
		count += 1
		count = count % len(protein_ids)

# TODO:
# 1. Draw amino acids
# 2. Draw by atom with (1) colors for atoms AND (2) colors for amino acids. 
# 3. Make drawing look nice, similar to what other softwares do. 
#	 Introduce different fidelities/speeds to draw, to allow interactive drawing when 
# 	 training e.g. a generative adversarial network. 
