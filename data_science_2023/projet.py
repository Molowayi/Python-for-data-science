#%% Importations
import pandas as pd
from pathlib import Path  
import matplotlib
matplotlib.use("agg")   # pour une meilleure gestion de l'affichage des graphique. Mettre ce code avant tous les autres import de matplotlib
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np
#%% 
folder = Path(__file__).parent
print(folder / "2018_sac_gas.csv")
df = pd.read_csv(folder / '2018_sac_gas.csv', sep=';')

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
print(infractions)
# %%
