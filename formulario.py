from bs4 import BeautifulSoup
import requests
import csv
URL_BASE = 'https://scrapepark.org/courses/spanish/contact'
input = []
for i in range(1,3):
    URL_FINAL = f"{URL_BASE}{i}"
    print(URL_FINAL)
    r = requests.get(URL_FINAL)
    soup = BeautifulSoup(r.text,"html.parser")
    todos_input = soup.find_all('input')
    for seccion in todos_input:
        input.append(seccion)
        print(seccion)
input.insert(0,"Etiqueta")
with open('archivos/formularios.csv','w') as temp_file:
    for item in input:
        temp_file.write("%s\n" % item)