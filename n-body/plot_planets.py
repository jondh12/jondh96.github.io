import numpy as np
import plotly.graph_objects as go


data = np.fromfile('data.dat', dtype=np.float64)

lim = 1e12

init_data = data[0:20]
init_x = init_data[0::2]
init_y = init_data[1::2]

fig = go.Figure()

fig = go.Figure(
    data=[go.Scatter(x=init_x, y=init_y,
                     mode="markers")],
    layout=go.Layout(
        xaxis=dict(range=[-lim, lim], autorange=False, zeroline=False),
        xaxis_title="X Position (m)",
        yaxis_title="Y Position (m)",
        yaxis=dict(range=[-lim, lim], autorange=False, zeroline=False),
        title_text="Planetary Motion",
        hovermode="closest",
        font=dict(
        # family="Courier New, monospace",
        size=18
        ),
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None, {"frame": {"duration": 0, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 0,
                                                                   "easing": "quadratic-in-out"}}]),
                                   dict(label="Pause",
                                        method="animate",
                                        args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                       "mode": "immediate",
                                                               "transition": {"duration": 0}}])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=data[100*20*k:100*20*k+20][0::2],
            y=data[100*20*k:100*20*k+20][1::2],
            mode="markers",
            marker=dict(color=["orange", "grey", "orange", "green", "red", "orange", "red", "purple", "blue", "purple"], size=[20, 10, 10, 10, 10, 16, 14, 16, 16, 10]))])

            for k in range(int(1e3))]
)

fig.write_html("planets.html", include_mathjax='cdn')
