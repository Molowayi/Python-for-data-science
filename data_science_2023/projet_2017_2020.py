#Préparation des données : conversion de format d'encodage du fichier. Adaptation de la ligne des montants €, changement du titre, NAN
#%% Importations et fonctions
import pandas as pd
from pathlib import Path  
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np

def je_fais_un_histogramme(df, nom_colonne):
    df[nom_colonne].hist(grid=True, xrot=90)
    
def un_histogramme(df, nom_colonne, titre, x_label, y_label):
    vc = df[nom_colonne].value_counts()
    print("vc : \n", vc)
    print("vc index : \n", vc.index)

    grand_font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 12,
    }   # https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
    font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 10,
    }
    petit_font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 8,
    }    
    plt.xlabel(x_label, fontdict=petit_font)
    plt.ylabel(y_label, fontdict=petit_font)
    plt.title(f"Effectifs des {titre}", fontdict=grand_font)
    plt.bar(vc.index, vc)
    # plt.xticks(rotation = 90)
    return plt
def je_fais_un_donut(titre, dataframe, nom_colonne):
    
    df_colonne = dataframe[nom_colonne].value_counts()
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = df_colonne.index 

    data = df_colonne  #[225, 90, 50, 60, 100, 5]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title(titre)

    # return mpl_to_plotly(fig)
    return plt

def je_fais_un_diagramme_circulaire(nom_colonne):
    pass



#%% Chargement données et création du data frame
if __name__ == '__main__':
    folder = Path(__file__).parent
    #print(folder / "2017_to_2020_sacgas.csv")
    df = pd.read_csv(folder / '2017_to_2020_sacgas.csv', sep=';')

    pd.set_option("display.min_rows", 10)

    # print(df)

    # print(df.describe())

 #   print(df["Montant total"])

#%% Voir combien de catégories de sanction il y a
    setCategories = set()
    for cat in df["Catégorie"]:
        setCategories.add(cat)
#    print(setCategories)
# %% Voir les différentes infractions et montants
    infractions = set()
    for cat in df["Infractions"]:
        infractions.add(cat)
    print("Il y a combien d'infractions ? ", len(infractions))
    # print(df.iat[1, 2] )
    # print(float(df.iat[1, 1].strip().replace(",", ".")))
    # print(type(df["Montant total"]))
    # print(len(df["Montant total"]))

    list_montants = []
    for m in df["Montant total"]:
        list_montants.append(float(m.strip().replace(",", ".")))
    s = pd.Series(list_montants)
    # print(s.describe())
    s.plot.hist()
    # plt.ylabel("Fréquence")
    # plt.xlabel("Montant contravention")
    # plt.title("Année 2018")
    # plt.hist(s)
    # s.hist()
    # %%
    df["Règlement"].hist(grid=True, xrot=90)
    # %%
    df["Catégorie"].hist()
    # plt.hist(df["Catégorie"])
    # %% Impression contenu des colonnes
    for nom in df.columns.to_list():
        leset = set()
        for ligne in df[nom]:
            leset.add(ligne)
        # print(nom, f" : {len(leset)} \n",leset)

    # print(df.columns.to_list())

    # %% Histogramme pour quelques colonnes
    # df_colonnes_pour_histogramme = df[["Catégorie", "Montant total", "Langue", "Règlement", "Infractions"]]
    # print(df_colonnes_pour_histogramme)
    #  df_colonnes_pour_histogramme["Montant total"].hist()
    # %% Histogramme des règlements
    un_histogramme(df,"Règlement","Réglements", "Réglement", "Effectif")
    # %% Histogramme pour quelques colonnes
    un_histogramme(df,"Langue","Langues", "Langue", "Effectif")
    # %% Histogramme pour quelques colonnes
    un_histogramme(df,"Année faits","années", "Année", "Effectif")
    # %% Histogramme pour quelques colonnes
    un_histogramme(df,"Montant total","Montant totaux", "Montant total", "Effectif")
    # %% Histogramme pour quelques colonnes
    un_histogramme(df,"Catégorie","Catégories", "Catégorie", "Effectif")
    # je_fais_un_histogramme("Règlement")
    # %% Diagramme circulaire des  montants : https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py
    df_montants = df["Montant total"].value_counts()
    # print(df_montants)
    # print(df_montants.index)
    # Carte Auderghem : https://www.google.com/maps/place/Auderghem/@50.8098864,4.4421555,14z/data=!4m6!3m5!1s0x47c3a7be0c453d4b:0x143c8e127699e0ed!8m2!3d50.8165284!4d4.4263428!16zL20vMDZuejZf?entry=ttu
    # %% Les fonctions qui créent les graphiques pour Dash (voir plus haut)
    je_fais_un_donut("Montants sanctions", df, "Montant total").show()
     # %%
    je_fais_un_histogramme(df, "Règlement")
# %%
