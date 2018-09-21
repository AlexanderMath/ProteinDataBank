from biopandas.pdb import PandasPdb
import sys

# Multi-Thread this for faster download. 
# See if one can download a list with all ids from www.rcbs.org, if not, make a webcrawler that fetches them all. 

def download_proteins(protein_ids, save_path):
	
	num = len(protein_ids)
	for i, id_ in enumerate(protein_ids): 
		print("[%i / %i]\tFetching '%s' ... \t"%(i+1, num, id_), end="", flush=True)
		ppdb = PandasPdb().fetch_pdb(id_)
		ppdb.to_pdb(save_path + id_ + ".pdb")
		print("DONE!")

if __name__ == "__main__":
	save_path 	= "proteins/"
	#protein_ids = ['5WA1', '5WFL', '5WFV', '5WG1'] # find more at www.rcbs.org

	import urllib.request
	import json
	url = "https://www.rcsb.org/pdb/json/searchresults.do?tabtoshow=Current&qrid=58684AA8"
	response = urllib.request.urlopen(url)
	a = json.loads(response.read())
	protein_ids = a["All Results"]

	download_proteins(protein_ids, save_path)

