from biopandas.pdb import PandasPdb
import sys

# Multi-Thread this for faster download. 
# See if one can download a list with all ids from www.rcbs.org, if not, make a webcrawler that fetches them all. 

def download_proteins(protein_ids, save_path):
	
	num = len(protein_ids)
	error_ids = []
	for i, id_ in enumerate(protein_ids): 
		print("[%i / %i]\tFetching '%s' ... \t"%(i+1, num, id_), end="", flush=True)
		try:
			ppdb = PandasPdb().fetch_pdb(id_)
			ppdb.to_pdb(save_path + id_ + ".pdb")
			print("DONE!")
		except: 
			error_ids.append(id_)
			print("\n\n\nBroke at id '%s'. The following list contains all breaks. \n"%id_, error_ids)

if __name__ == "__main__":
	save_path 	= "proteins/"
	#protein_ids = ['5WA1', '5WFL', '5WFV', '5WG1'] # find more at www.rcbs.org

	f = open("protein_ids.txt", "r")
	protein_ids = eval(str(f.read())) # it is stored as list.
	print(protein_ids)
	
	download_proteins(protein_ids, save_path)

