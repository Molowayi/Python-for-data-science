#%%
import pandas as pd
from pathlib import Path    # dans Path, ils ont défini la notion de division du chemin
# pd.options.display.max_rows = None

print(__file__)
folder = Path(__file__).parent
print(folder / "countries.csv")
data = pd.read_csv(folder / 'countries.csv') # ici on a le séparateur par défaut qui est la virgule, donc on peut ne pas l'écrire. Si le cvs était dans un sous dossier du dossier où se trouve le fichier python, on aura par exemple "data/countries.py"
# data = pd.read_csv('rC:\Users\STG3802\Documents\src\data_science_2023\countries.csv') # ici on a le séparateur par défaut qui est la virgule, donc on peut ne pas l'écrire

# pd.set_option("display.max_rows", None) # pour les options d'affichage. None signifie qu'il n'y a pas de limite
pd.set_option("display.min_rows", 20) # pour les options d'affichage. None signifie qu'il n'y a pas de limite

print ("Les data \n",data)

print("Les colonnes \n",data.columns)     # imprime les noms des colonnes. On peut alors extraire les colonnes qu'on veut.

# pd.reset_option("all") pour remettre à l'état initial (valeur par défaut) une option ou toutes

#%%

# scatter plot
import pandas as pd
from pathlib import Path  
import matplotlib.pyplot as plt
# print(__file__)
folder = Path(__file__).parent
# print(folder / "countries.csv")
data = pd.read_csv(folder / 'countries.csv')
plt.plot(data.Population, data["GDPPC"], ".")    # On peut aussi sélectionner les colonnes par iloc ou loc
plt.show()

# plt.plot(boxplot(data.Literacy, 0, "")) # pour le diagramme à moustaches

# %%
