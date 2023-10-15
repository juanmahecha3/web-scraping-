from bs4 import BeautifulSoup
import requests
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido =  pedido_obtenido.text
soup1 = BeautifulSoup(html_obtenido,"html.parser")
src_todos = soup1.find_all(src=True)
#Etiquetas Imagenes
for elemento in src_todos:
    if (elemento['src'].endswith(".png")) or (elemento['src'].endswith("jpg")):
        print(elemento)
#Almacenar imagenes
url_imagenes =[]
for i, imagen in enumerate(src_todos):
    if imagen['src'].endswith("png"):
        print(imagen['src'])
        r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
        with open(f'imagenes/imagen_{i}.png','wb') as f:
            f.write(r.content)

    if imagen['src'].endswith("jpg"):
        print(imagen['src'])
        r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
        with open(f'imagenes/imagen_{i}.jpg','wb') as f:
            f.write(r.content)