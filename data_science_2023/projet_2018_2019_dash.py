#%%
import matplotlib
matplotlib.use("agg")   # pour une meilleure gestion de l'affichage des graphique. Mettre ce code avant tous les autres import de matplotlib
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np
# from projet_2018_2019 import je_fais_un_donut
import projet_2018_2019 as pj
#%% Création du graph


#graph_ex = dcc.Graph(figure=pj.je_fais_un_donut(), id="graph_")

#%% Création de la page web
extra_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=extra_css)   # L'attribut name permet d'utiliser du CSS. ajouter le dossier assets dedans le fichier style.css
app.layout = html.Div([html.H1("Sanctions administratives communales"), 
                       html.Div([html.P("Hello paragraphe", id="leparagraphe_test", className="box"),
                                 html.P("Hello paragraphe", id="leparagraphe_test2", className="box"),
                       dcc.RadioItems(["2017", "2018", "2019", "2020"], value="2018", id="annee"),
                       dcc.Dropdown(
                           options={
                               "auderghem":"Auderghem",
                               "ixelles":"Ixelles",
                               "saintgilles":"Saint Gilles",
                           },
                           value="Auderghem", id="commune"
                       ),
                       dcc.Graph(figure=pj.je_fais_un_donut(), id="graph_"), ],
                       className="box")])
#     dcc.Graph(figure=create_graph,id="graph")

@app.callback(Output("leparagraphe_test", "children"), [Input("annee", "value")])
def update_paragraph(radio_value):
    return f"{radio_value}"

@app.callback(
        Output("leparagraphe_test2", "children"), Input("commune", "value"))
def update_graph(dropdown_value):
    return f"{dropdown_value}"

# @app.callback(
#         Output("graph_", "children"), Input("commune", "value"))
# def update_graph(dropdown_value):
#     pass

# Les deux lignes suivantes doivent venir à la fin du script car quand il exécute ces lignes, il entre dans une boucle sans fin
if __name__ == '__main__':
    app.run_server(debug=True)