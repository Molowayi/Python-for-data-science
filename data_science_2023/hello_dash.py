import matplotlib
matplotlib.use("agg")   # pour une meilleure gestion de l'affichage des graphique. Mettre ce code avant tous les autres import de matplotlib
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np

# def create_sine_graph():
def create_sine_graph(n=3, style="r--"):
    fig, ax = plt.subplots()
    ax.set_title("Sine Wave Form")
    x = np.arange(0, n*np.pi, 0.1)  # avant, n était 3
    ax.plot(x, np.sin(x), style)

    return mpl_to_plotly(fig)

foot = html.Div("Footer") # On fait des variables pour palier au fait que l'arbre devient trop chargé; on peut même exporter dans un fichier extérieur
extra_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=extra_css)   # L'attribut name permet d'utiliser du CSS. ajouter le dossier assets dedans le fichier style.css
app.layout = html.Div(html.H1("Hello, Dash!"), 
                       html.Div(html.P("Hello paragraphe"), className="box"),
                       html.Div([html.Span("Ici un span"),
                       dcc.Slider(0, 10, 0.1, value=5, id="slider1"),
                       html.P("Valeur du slider ici", id="p-slider"),
                       dcc.RadioItems(["Color", "Line"], value="Color", id="style-select"),
                       dcc.Dropdown(
                           options={
                               "r--":"Red",
                               "b-":"Blue, plain line",
                               "g.-":"Green, dotted",
                           },
                           value="r--", id="graph-style"
                       ) ,
                    
                       dcc.Graph(figure=create_sine_graph(), id="sine-graph"),
                       foot,], className="box") )

import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly

@app.callback(Output("p-slider", "children"), [Input("slider1", "value")])
def update_paragraph(slider_value):
    return f"Slider selected {slider_value}"


@app.callback(
        Output("sine-graph", "figure"), [Input("slider1", "value"), Input("graph-style", "value")])
def update_graph(slider_value, dropdown_value):
    return create_sine_graph(slider_value, dropdown_value)

@app.callback(Output("graph-style", "options"),[Input("style-select", "value")])
def updater_dropdown_options(radio_value):
    if radio_value == "Color":
        return {"r": "Red", "g":"Green", "b":"Blue"}
    
    elif radio_value == "Line":
        return {"-":"Plain", ".-":"Dotted", "--":"Dashed"}

# Les deux lignes suivantes doivent venir à la fin du script car quand il exécute ces lignes, il entre dans une boucle sans fin
if __name__ == '__main__':
    app.run_server(debug=True)