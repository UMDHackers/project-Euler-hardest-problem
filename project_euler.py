#C:/Phyton27/ 
import re
import urllib2
from bs4 import BeautifulSoup

def parseNavBar(rawCode):
	soup = BeautifulSoup(rawCode, 'html.parser')
	#soup.prettify()
	navbar = []
	for i in soup.findAll('a'):
		if "archives;" in i.get("href"):
			navbar.append(i)
	return navbar
	
def pageParser(page):
	anchor = str(page).split(" ")
	href = anchor[1]
	page_link = re.search('href="(\S+)"', href)
	return page_link.group(1)
	
def parseProblemLinks(page_link):
	pageX = urllib2.urlopen('http://projecteuler.net/'+page_link)
	pageX_html = page_link.read()
	soup = BeautifulSoup(pageX_html, 'html.parser')
	problems = []
	for i in soup.findAll('tr'):
		if "problem" in i.get("href"):
			print i
			problems.append(i)
	return problems
	
	
	
	
	
#Get core HTML of the first page
f= urllib2.urlopen('http://projecteuler.net/archives')

#Get the navbar
navbar = parseNavBar(f.read())

#Go through nav-bar and remove duplicates
page_links = []
for page in navbar:
	if page not in page_links:
		page_link.append(pageParser(page))
	else: 
		break

#page_links = list(set(page_links))

for link in page_links:
	print parseProblemLinks(link)
	
	
	

