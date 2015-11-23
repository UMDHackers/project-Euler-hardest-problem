#C:/Phyton27/
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
#Get core HTML
f= urllib2.urlopen('http://projecteuler.net/archives')

#Get the navbar
navbar = parseNavBar(f.read())

#
