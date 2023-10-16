from bs4 import BeautifulSoup
import requests
import re

URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text
soup = BeautifulSoup(html_obtenido,"html.parser")
menu = soup.find(string=re.compile("MENÚ"))
print(menu.parent.find_next_siblings())