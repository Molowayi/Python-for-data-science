from bs4 import BeautifulSoup
import requests

url = "https://scrapethissite.com/pages/simple/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")

for title in soup.find_all("h3"):       # find tout court prend uniquement la première occurrence
    # print(title)                        # title est un objet tag (Essayer de l'afficher)
    print(title.text.strip())
    print(title.find("i", class_ = "flag-icon"))    # on peut passer id s'il y en a, ou un dictionnaire d'attribut {"id":toto, "class": "country"}
    print(title.find("span"))

    # d = {

    #     "colomn1" : [...],
    #     "colomn2" : [...],
    #     "colomn3" : [...]
    # }
