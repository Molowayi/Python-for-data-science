#%%
import pandas as pd
import requests
import json # ce module est dans la librairie standard. Pas besoin de l'installer avec pip
import matplotlib.pyplot as plt
r = requests.get("https://api.frankfurter.app/2023-09-01..2023-10-31?to=USD")
# print(r.text)

data = json.loads(r.text)   # transforme le texte reçu en objet Python, ici un dictionnaire
# print(data)
# plt.plot(data.rates, data.rates.USD, ".") 
# plt.show()

data2 = data["rates"]
print(data2)
#%%
indexes = [n for n in data2]    # to_datetime convertit les dates en string en datetime
data_taux = [n["USD"] for n in data2.values()]
df = pd.Series(data_taux, index = indexes)

# %%
plt.plot(indexes, data_taux, ".") 

# %%
plt.plot(df.index, df, ".") 

#%%
