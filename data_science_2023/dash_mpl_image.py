import matplotlib
matplotlib.use("agg")
import io
import base64
import dash
from dash import html, dcc
import numpy as np
import matplotlib.pyplot as plt

app = dash.Dash(__name__)
    
app.layout = html.Div(children=[
    html.Img(id='test'), # img element
        dcc.Slider(
        id='n_points',
        min=1,
        max=10,
        step=1,
        value=5,
    ),
])

@app.callback(
    dash.dependencies.Output('test', 'src'), # src attribute
    [dash.dependencies.Input('n_points', 'value')]
)
def update_figure(n_points):
    #create some matplotlib graph
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)
    buf = io.BytesIO() # in-memory files
    plt.scatter(x, y)
    plt.savefig(buf, format = "png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8") # encode to html elements
    buf.close()
    return "data:image/png;base64,{}".format(data)

if __name__ == "__main__":
    app.run_server(debug=True)