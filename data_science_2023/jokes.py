import requests
import json # ce module est dans la librairie standard. Pas besoin de l'installer avec pip
r = requests.get(
"https://official-joke-api.appspot.com/random_joke")
print(r.text)
joke = json.loads(r.text)
print(joke) # Python affiche les dictionnaires par défaut avec les simples guillemets dans le terminal
for k, v in joke.items():
    print(f"{k} : {v}")