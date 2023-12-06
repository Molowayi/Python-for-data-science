import matplotlib
matplotlib.use("agg")

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np

def create_sine_graph(n=3, style="r--", func=np.sin):
    fig, ax = plt.subplots()

    x = np.arange(0, n*np.pi, 0.1)
    ax.plot(x, func(x), style)
    ax.set_title("Sine graph")

    return mpl_to_plotly(fig)


title = html.H1([
    html.Span("Hello"),
    ", Dash!",
])

extra_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=extra_css)

app.layout = html.Div([
    title,
    
    html.Div(html.P("This is the intro."), className="box"),
    html.Div([
        dcc.Slider(0, 10, 1, value=5, id="slider1"),
        html.P("Valeur du slider ici!", id="p-slider"),
        dcc.RadioItems(["Color", "Line"], value="Color", id="style-select"),
        dcc.Dropdown(
        options = {
            "r--": "Red, dashed",
            "b-": "Blue, plain line",
            ".-g": "Green, dotted",
        }, value="r--", id="graph-style", clearable=False
    ),
        dcc.Graph(figure=create_sine_graph(), id="sine-graph"), 
        ], className="box"),
    ])

@app.callback(Output("p-slider", "children"), [Input("slider1", "value")])
def update_paragraph(slider_value):
    return f"Slider selected {slider_value}"

@app.callback(
        Output("sine-graph", "figure"),
        [Input("slider1", "value"), Input("graph-style", "value")])
def update_graph(slider_value, dropdown_value):
    funcs = {
        "sin": np.sin,
        "cos": np.cos,
    }

    return create_sine_graph(slider_value, dropdown_value)

@app.callback(Output("graph-style", "options"), [Input("style-select", "value")])
def update_dropdown_options(radio_value):
    if radio_value == "Color":
        return {"r": "Red", "g": "Green", "b": "Blue"}
    elif radio_value == "Line":
        return {"r-": "Plain", "r.-": "Dotted", "r--": "Dashed"}


if __name__ == "__main__":
    app.run_server(debug=True)


