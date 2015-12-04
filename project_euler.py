#C:/Phyton27/ 
#find hardest problem on projecteuler, based on diffcult source code

import re
import urllib2
from bs4 import BeautifulSoup
from operator import attrgetter
class Problem:
	def __init__(self, number, diffculty, page, solved_by):
		self.number = number
		self.diffculty = diffculty
		self.page = page
		self.solved_by = solved_by
	
#Globals
problem_urls = dict()
problems_list = list()
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
	
def parseProblemPages(link):
	problem_page = urllib2.urlopen('http://projecteuler.net/'+link)
	pageX_html = problem_page.read()
	soup = BeautifulSoup(pageX_html, 'html.parser')
	link_number = re.search('problem=(\S+)', link).group(1)
	for i in soup.findAll('span'):
		if "Published" in str(i):
			string_list = str(i).split(";")
			solved_by = re.search(' Solved by (\S+)', string_list[1]).group(1)
			diffculty = re.search(' Difficulty rating: (\S+)%', string_list[2]).group(1)
			diffculty = int(diffculty)
			page = re.search('archives;page=(\S+)',problem_urls[link])
			if page:
				page = page.group(1)
			else:
				page = "1"
			temp_pro = Problem(link_number, diffculty, page, solved_by)
			problems_list.append(temp_pro)

	
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

#add the first page
page_links.append("archives")

#find all problem links
for link in page_links:
	parseProblemLinks(link)

#make obj for each problem
for prb in problem_urls.keys():
	parseProblemPages(prb)

problems_list.sort(key=attrgetter('diffculty', 'solved_by'), reverse=True)
print "Top 50 hardest problems"
for i in range(0,50):
	current = problems_list[i]
	num = str(i + 1)
	prb_num = current.number
	page_num = current.page
	diffculty = str(current.diffculty)
	solved_by = current.solved_by
	print "Number " + num + ", Problem Number "+ prb_num + ", Page number " + page_num +", diffculty " + diffculty + "%, Solved by " + solved_by


