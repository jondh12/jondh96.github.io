import numpy as np
import plotly.graph_objects as go


data = np.fromfile('data.dat', dtype=np.float64)

lim = 1e11

init_data = data[0:20]
init_x = init_data[0::2]
init_y = init_data[1::2]

fig = go.Figure()

fig = go.Figure(
    data=[go.Scatter(x=init_x, y=init_y,
                     mode="markers")],
    layout=go.Layout(
        xaxis=dict(range=[-lim, lim], autorange=False, zeroline=False),
        yaxis=dict(range=[-lim, lim], autorange=False, zeroline=False),
        title_text="Planetary Motion", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=data[100*20*k:100*20*k+20][0::2],
            y=data[100*20*k:100*20*k+20][1::2],
            mode="markers",
            marker=dict(color="red", size=10))])

        for k in range(int(100))]
)

fig.write_html("planets.html")
