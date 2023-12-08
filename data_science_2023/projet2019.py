#%% Importations
import pandas as pd
from pathlib import Path  
# import matplotlib
# matplotlib.use("agg")   # pour une meilleure gestion de l'affichage des graphique. Mettre ce code avant tous les autres import de matplotlib
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np
#%% 
folder = Path(__file__).parent
print(folder / "2019_sac_gas-ameliore.csv")
df = pd.read_csv(folder / '2019_sac_gas-ameliore.csv', sep=';')

pd.set_option("display.min_rows", 10) 

print(df)

print(df.describe())

print(df["MontantTotalEuros"])

#%% Voir combien de catégories de sanction il y a
setCategories = set()
for cat in df["Catégorie"]:
    setCategories.add(cat)
print(setCategories)
# %% Voir les différentes infractions
infractions = set()
for cat in df["Infractions"]:
    infractions.add(cat)
print("Il y a combien d'infractions ? ", len(infractions))
print(df.iat[1, 2] )
print(float(df.iat[1, 1].strip().replace(",", ".")))
print(type(df["MontantTotalEuros"]))
print(len(df["MontantTotalEuros"]))

list_montants = []
for m in df["MontantTotalEuros"]:
    list_montants.append(float(m.strip().replace(",", ".")))
s = pd.Series(list_montants)
print(s.describe())
# s.plot.hist()
# plt.ylabel("Fréquence")
# plt.xlabel("Montant contravention")
# plt.title("Année 2018")
# plt.hist(s)
# s.hist()
df["Règlement"].hist()
print()
# df["Catégorie"].hist()
# plt.hist(df["Catégorie"])
# %% Impression contenu des colonnes
# for nom in df.columns.to_list():
#     leset = set()
#     for ligne in df[nom]:
#         leset.add(ligne)
#     print(nom, f" : {len(leset)} \n",leset)

# print(df.columns.to_list())

# %% Histogramme pour quelques colonnes
# df_colonnes_pour_histogramme = df[["Catégorie", "MontantTotalEuros", "Langue", "Règlement", "Infractions"]]
# print(df_colonnes_pour_histogramme)
#  df_colonnes_pour_histogramme["MontantTotalEuros"].hist()
# %% Histogramme des règlements
vc = df["Règlement"].value_counts()
print("vc : \n", vc)
print("vc index : \n", vc.index)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 12,
        }   # https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html

plt.xlabel("Règlement enfreint", fontdict=font)
plt.ylabel("Fréquences")
plt.title("Fréquences des infractions aux différents règlements", fontdict=font)
# plt.bar(vc.index, vc)
plt.bar(["AUDERGHEM-RGP", "CODE DE LA ROUTE", "POLICE BXL"], vc)
plt.xticks(rotation = 40)
plt.show()
# %% Histogramme des fréquences par adresse (Pour voir quels endroits sont les plus dangereux)
# Carte Auderghem : https://www.google.com/maps/place/Auderghem/@50.8098864,4.4421555,14z/data=!4m6!3m5!1s0x47c3a7be0c453d4b:0x143c8e127699e0ed!8m2!3d50.8165284!4d4.4263428!16zL20vMDZuejZf?entry=ttu
