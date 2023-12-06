#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("social_network_data.csv")
df_filtered = df[df["friends"] < 100]
# print(df)
vc = df.value_counts()
# print(vc)   # donne le nombre de personnes ayant x amis passant y temps sur les réseaux sociaux
#%%
# pour compter seulement les amin
vc = df["friends"].value_counts()   # donne le compte du n d'amis et le n des personnes les ayant
# print(vc)
#%%
plt.bar(vc.index, vc)
# plt.show()

#%%
# print(df.sort_values(by=["friends","minutes"])) # by est facultatif; on peut donner une liste de titres. mettre - devant les entêtes pour
# %%
# print(df.mean())    # donne la moyenne de chaque colonne

# print(df[df["friends"] < 100].mean())  # On exclut la donnée abérante ici classée en première ligne
# %%
# print(df.median())
# print(df_filtered.median())
# print(df.quantile(0.25))
# print(df.var())
# print(df_filtered.var())
# print(df.std())
# %%
print(df.describe())    # df.describe() donne est un dataframe
print(df_filtered.describe())

print(df.cov())
print(df_filtered.cov())
print(df.corr())    # On voit que la corrélation est positive, la donnée abérante (outlier) a grande influence, (dans le contexte des réseaux sociaux) cette donnée est peut-être un robot ou un utilisateur qui n'a plus de temps
print(df_filtered.corr())

q1 = df["friends"].quantile(0.25)
q3 = df["friends"].quantile(0.75)
# interval = (q1-1.5*(q3-q1), q3+1.5*(q3-q1))
interval = (q1-3*(q3-q1), q3+3*(q3-q1))
print(interval)
#%% 
# Polynomial regression
from numpy.polynomial import Polynomial

p = Polynomial.fit(df["friends"], df["minutes"], 2)
print("Les poynomes, \n", p)
print(p.convert())  # car p est fourni avec des coefficient du changement d'intervalle des données sur la fenêtre [-1,1]
print(p(0))
coeff = p.convert().coef
print("Les coefficients : \n", coeff)
print(p.coef) # les coefficients dans la transformation de l'intervalle dans le window [-1, 1]
print("Les fenêtres")
print(p.window)
print(p.domain)
p,info = Polynomial.fit(df["friends"], df["minutes"], 8, full=True)
print("Les infos", info)
#%% 
# Graphe données et polynome. Un scatter qui donne les points
x = df["friends"]
x = np.linspace(0,110,200)
plt.scatter(df["friends"], df["minutes"], 1)
plt.plot(x, p(x),"r")
plt.show()
