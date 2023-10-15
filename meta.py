# Importar BeutifulSoup y requests
from bs4 import BeautifulSoup
import requests

# Empezamos en Scraping
# 1 Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido,"html.parser")

todos_meta = soup.find_all('meta')

# Iterar sobre el objeto
for seccion in todos_meta:
    print(seccion)