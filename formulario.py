from bs4 import BeautifulSoup
import requests
URL_BASE = 'https://scrapepark.org/courses/spanish/contact'
for i in range(1,3):
    URL_FINAL = f"{URL_BASE}{i}"
    print(URL_FINAL)
    r = requests.get(URL_FINAL)
    soup = BeautifulSoup(r.text,"html.parser")
    todos_input = soup.find_all('input')
    # Iterar sobre el objeto
    for seccion in todos_input:
        print(seccion)