from __future__ import print_function
import pickle
import requests
from BeautifulSoup import BeautifulSoup

#print list
def readlist(list_of_rows):
    infile = open("./proxylist.p", "rb")
    list_of_rows = pickle.load(infile)
    i=0
    for row in list_of_rows:
	print(*list_of_rows[i], sep='    ')
        i = i+1
    return
def main_menu():
    print ('1: Read Last Save')
    print ('2: Update Save ')
    print ('3: Exit')
    choice = input(":")
    return choice

choice =  main_menu()
while choice != 3:
	if choice == 2:
		url = 'https://incloak.com/proxy-list/' # Source of proxy list incloak.com
		response = requests.get(url)
		html = response.content

		soup = BeautifulSoup(html)
		table = soup.find('tbody') 
		number_of_rows = 0
		list_of_rows = []
		for row in table.findAll('tr'):
		    list_of_cells = []
		    i=0
		    for cell in row.findAll('td'):
			i = i+1
		    	text = cell.text.replace('&nbsp;', '')
			if i==1 or i==2 or i==5:
		    	    list_of_cells.append(text)
		    order=[2,0,1]
		    list_of_cells = [ list_of_cells[i] for i in order]
		    list_of_rows.append(list_of_cells)
		    number_of_rows = number_of_rows + 1

		outfile = open("./proxylist.p", "wb")
		pickle.dump(list_of_rows, outfile)
		outfile.close()
	else:
	    readlist("void")
	choice =  main_menu()

