from biopandas.pdb import PandasPdb
import sys

# Multi-Thread this for faster download. 

def download_proteins(protein_ids, save_path):
	
	num = len(protein_ids)
	for i, id_ in enumerate(protein_ids): 
		print("[%i / %i]\tFetching '%s' ... \t"%(i+1, num, id_), end="", flush=True)
		ppdb = PandasPdb().fetch_pdb(id_)
		ppdb.to_pdb(save_path + id_ + ".pdb")
		print("DONE!")

if __name__ == "__main__":
	save_path 	= "proteins/"
	protein_ids = ['5WA1', '5WFL', '5WFV', '5WG1'] # find more at www.rcbs.org
	download_proteins(protein_ids, save_path)

