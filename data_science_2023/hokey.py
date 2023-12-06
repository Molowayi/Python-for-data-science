from bs4 import BeautifulSoup
import requests

url = "http://www.scrapethissite.com/pages/forms/"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")

table = soup.find("table")
# print(table)

for titre in table.find_all("th"):
    print(titre.text.strip())






# for title in soup.find_all("h3"):       # find tout court prend uniquement la première occurrence
#     # print(title)                        # title est un objet tag (Essayer de l'afficher)
#     print(title.text.strip())
#     print(title.find("i", class_ = "flag-icon"))
#     print(title.find("span"))

    # d = {

    #     "colomn1" : [...],
    #     "colomn2" : [...],
    #     "colomn3" : [...]
    # }


# 1. voir années, voir si nouvelle équipe ou équipe qui arrête
# 2. il y a combien de pages? Jouer éventuellement sur le nombre de ligne par page. Les requettes de chargement de pages prennent bcp de temps. On peut mm avoir toutes les données sur la mm page car c'est permis dans ce exercice
# attention les pages commencent par n

# num_page =1
# f"http ....{num_page}"
# pour compter les nombre d'équipe? Soit utiliser un set car pas de duplication, la taille du set est le nombre d'équipe; soit une liste avec un if empêchant les duplications
#  
# team_names =set()
# team_names.add("toto")