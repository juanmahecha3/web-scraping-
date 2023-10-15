# Importar BeutifulSoup y requests
from bs4 import BeautifulSoup
import requests
# Empezamos en Scraping
# 1 Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text
# 2. "Parsear" ese HTML
soup1 = BeautifulSoup(html_obtenido,"html.parser")

src_todos = soup1.find_all(src=True)
for elemento in src_todos:
    if (elemento['src'].endswith(".png")) or (elemento['src'].endswith("jpg")):
        print(elemento)