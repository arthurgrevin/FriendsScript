from bs4 import BeautifulSoup  
import sys


input = sys.stdin
soup = BeautifulSoup(input,'html.parser')
lines = soup.find_all('p')

for line in lines :
	brut = line.text.encode('utf-8').strip()
	data = brut.split(':')
	if len(data)==2:
		character,text = data
		print '{}|{}'.format(character,text)		
	elif len(data)==4:
		character = data[0]
		text = data[1]+data[2]
		print '{}|{}'.format(character,text)
