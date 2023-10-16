from bs4 import BeautifulSoup
import requests
import csv
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text
soup = BeautifulSoup(html_obtenido,"html.parser")
todos_meta = soup.find_all('meta')
meta = []
for seccion in todos_meta:
    meta.append(seccion)
    print(seccion)
meta.insert(0,"Etiqueta")
with open('archivos/metadatos.txt','w') as temp_file:
    for item in meta:
        temp_file.write("%s\n" % item)