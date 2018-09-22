#-*-coding:utf8-*-
'''
Eduardo Freire Mangabeira
Descrição: O professor fernando nos mostrou parte esse código ano passado 
e agora consigo fazer com mais detalhes :)

	O programa coleta a flutuação(provavelmente fictícia) do preço do feijão a cada 15 minutos
	e escreve num arquivo csv.
'''
import time
import requests
import csv
from bs4 import BeautifulSoup as bs

t = requests.get("http://beans.itcarlow.ie/prices.html")
soup = bs(t.text, 'html.parser')

while(True):
	for price in soup.find_all('strong'):
		prices = price.get_text()
		print(prices)

	with open('beans.csv', 'a', newline='') as csvfile:
		bean_price = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		bean_price.writerow([prices])
    

	time.sleep(5)
