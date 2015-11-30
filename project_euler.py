#C:/Phyton27/ 
import re
import urllib2
from bs4 import BeautifulSoup

class Problem:
	

#Global
problem_urls = dict()

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
	pageX_html = pageX.read()
	soup = BeautifulSoup(pageX_html, 'html.parser')
	#print soup.prettify()
	for i in soup.findAll('a'):
		if "problem=" in i.get("href"):
			anchor = str(i).split(" ")
			href = anchor[1]
			temp = re.search('href="(\S+)"', href)
			prbl = temp.group(1)
			#print prbl
			problem_urls[prbl] = page_link
	
	
#def makeObjofProblem(prbl_link):
	
#Get core HTML of the first page
f= urllib2.urlopen('http://projecteuler.net/archives')

#Get the navbar
navbar = parseNavBar(f.read())

#Go through nav-bar 
page_links = []
for page in navbar:
	page_links.append(pageParser(page))

#remove duplicates
page_links = list(set(page_links))

#find all problem links
for link in page_links:
	parseProblemLinks(link)

#make obj for each problem
for prb in problem_urls.keys():
	print prb

	

