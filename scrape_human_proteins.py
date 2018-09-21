
# Go to http://www.rcsb.org and find the id of all human proteins, there are approximately 36000


'''import urllib.request
from html.parser import HTMLParser
response = urllib.request.urlopen('http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid=A39172A1')
html = response.read()

class FindIdParser(HTMLParser): 

	def handle_starttag(self, tag, attrs):
		if tag == "h3": 
			print("Start tag:", tag)

# Problem; the proteins cells in the homepage seems to be loading with JS after DOM is constructed, so the html code does not contain the proteins. 
print(str(html))
parser = FindIdParser()
parser.feed(str(html))
parser.close()'''

# Their page attempts to load proteins by doing an AJAX call to get all ids. 
# By inspecting the console of the page, I learned the list with all ids are obtained
# through
# https://www.rcsb.org/pdb/json/searchresults.do?tabtoshow=Current&qrid=58684AA8
# There are 31000 entries, it seems these are specific for humans ("homo sapiens only")

import urllib.request
import json
url = "https://www.rcsb.org/pdb/json/searchresults.do?tabtoshow=Current&qrid=58684AA8"
response = urllib.request.urlopen(url)
a = json.loads(response.read())
ids = a["All Results"]
print(len(ids))
