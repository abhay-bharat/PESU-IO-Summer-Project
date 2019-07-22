
from bs4 import BeautifulSoup as bs
import requests
import urllib
import csv
from lxml import html

url = 'https://karki23.github.io/Weather-Data/assignment.html'
base_link = 'https://karki23.github.io/Weather-Data/'
r = requests.get(url, headers = {'User-Agent':'Not blank'})
data = r.text
soup = bs(data, 'lxml')

hplinks = []
links = soup.find_all('a')

for l in links:
	hl = base_link + (l.get('href'))
	hplinks.append(hl)

print(hplinks)

response = requests.get(hplinks[0])
s = bs(response.content , 'html.parser')

filename = 'sample.csv'
csv_writer = csv.writer(open(filename, 'w'))

for tr in s.find_all("tr"):
	data = []
	for th in tr.find_all("th"):
		data.append(th.text)
	if data:
		print("inserting headers : {}".format(','.join(data)))
		csv_writer.writerow(data)
		continue
	for td in tr.find_all("td"):
		data.append(td.text.strip())
	if data:
		print("Inserting data :{}".format(','.join(data)))
		csv_writer.writerow(data)

for i in range((len(hplinks)) - 1):
	i+=1
	response = requests.get(hplinks[i])
	s = bs(response.content , 'html.parser')
	
	for tr in s.find_all("tr"):
		data = []
		for th in tr.find_all("th"):
			data.append(th.text)
		if data:
			continue
		for td in tr.find_all("td"):
			data.append(td.text.strip())
		if data:
			print("Inserting data :{}".format(','.join(data)))
			csv_writer.writerow(data)