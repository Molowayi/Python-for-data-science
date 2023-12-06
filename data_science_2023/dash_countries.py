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
# Polynôme
from numpy.polynomial import Polynomial

def regression(x,y):
    return Polynomial.fit(data[x], data[y], 2)
            # coeff = p.convert().coef

folder = Path(__file__).parent
print(folder / "countries.csv")
data = pd.read_csv(folder / 'countries.csv')

pd.set_option("display.min_rows", 20) 

# print ("Les data \n",data)

colonnes = data.columns
# for colonne in colonnes:
#     print(colonne)

def create_countries_graph(abscisses =data["GDPPC"], ordonnees = data["Agriculture"], style = "-"):
    fig, ax = plt.subplots()
    # ax.set_title(f"{ordonnees} en fonction de {abscisses}")
    x = abscisses  
    ax.plot(x, ordonnees, style)
    return mpl_to_plotly(fig)

extra_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=extra_css)   # L'attribut name permet d'utiliser du CSS. ajouter le dossier assets dedans le fichier style.css
app.layout = html.Div([html.H1("Countries"), 
                       
                       html.Div([
                                        
                            dcc.Dropdown(
                                options={
                                    "Country" :  "Country",
                                    "Name"  : "Name",
                                    "GDPPC" :  "GDPPC",
                                    "Literacy" : "Literacy",
                                    "InfantMortality"  : "InfantMortality",
                                    "Agriculture" :   "Agriculture",
                                    "Population" : "Population",
                                    "NetMigration" :  "NetMigration",
                                },
                                value="GDPPC", id="graph-axis"
                            ) ,
                            dcc.Dropdown(
                                options={
                                    "Country" :  "Country",
                                    "Name"  : "Name",
                                    "GDPPC" :  "GDPPC",
                                    "Literacy" : "Literacy",
                                    "InfantMortality"  : "InfantMortality",
                                    "Agriculture" :   "Agriculture",
                                    "Population" : "Population",
                                    "NetMigration" :  "NetMigration",
                                },
                                value="Agriculture", id="x-axis"
                            ) ,
                    
                            dcc.Graph(figure=create_countries_graph(), id="country-graph"),
                            html.P("", id="warning"), html.P("", id="polynom")
                       ], className="box") ])


@app.callback(Output("country-graph", "figure"), [Input("graph-axis", "value")])
def update_paragraph(y_axis):
    return create_countries_graph(ordonnees= data[y_axis])

@app.callback(Output("country-graph", "figure"), [Input("x-axis", "value")])
def update_paragraph(xx_axis):
    return create_countries_graph(abscisses= data[xx_axis])

@app.callback(Output("polynom", "children"), [Input("x-axis", "value")])
def update_polynom(xx_axis):
    return create_countries_graph(abscisses= data[xx_axis])






if __name__ == '__main__':
    app.run_server(debug=True)