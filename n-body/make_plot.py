import numpy as np
import plotly.graph_objects as go

n = 1000

x = np.linspace(0, 1, n)
y = np.random.randn(n)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='test'))
fig.update_layout(
        title="Test Plot",
        xaxis_title="X",
        yaxis_title="Y")

fig.write_html("test_plot.html")
