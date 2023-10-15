# Importar BeutifulSoup y requests
from bs4 import BeautifulSoup
import requests

import bs4 # solo para chequeo
print(" Versión de BeatifulSoup: ", bs4.__version__)
print(" Versión de requests: ", requests.__version__)

# Empezamos en Scraping
# 1 Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido,"html.parser")