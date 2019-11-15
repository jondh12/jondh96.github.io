import pandas as pd
import plotly.graph_objects as go
import numpy as np
# import plotly.graph_objects as go

n = 100

x = np.linspace(-1, 3, n)
y = np.exp(x)
y0 = (0, 1)
y1 = (1, 2)
y2 = (2, 4)
y3 = (3, 8)


# fig.add_trace(go.Scatter(visible=True, name="Truth", x=x, y=y))
# fig.add_trace(go.Scatter(visible=False, name="Step 1", line=dict(color='red'), x=[y0[0],y1[0]], y=[y0[1], y1[1]]))
# fig.add_trace(go.Scatter(visible=False, name="Step 2", line=dict(color='purple'), x=[y1[0],y2[0]], y=[y1[1], y2[1]]))
# fig.add_trace(go.Scatter(visible=False, name="Step 3", line=dict(color='green'), x=[y2[0],y3[0]], y=[y2[1], y3[1]]))

f1 = go.Frame(name ="f1", data=[go.Scatter(x=x, y=y, line=dict(color='purple'))])
f2 = go.Frame(name ="f2", data=[go.Scatter(visible=True, name="Step 1", line=dict(color='red'), x=[y0[0],y1[0]], y=[y0[1], y1[1]])])
f3 = go.Frame(name ="f3", data=[go.Scatter(visible=True,name="Step 2", line=dict(color='purple'), x=[y1[0],y2[0]], y=[y1[1], y2[1]])])
f4 = go.Frame(name ="f4", data=[go.Scatter(name="Step 3", line=dict(color='green'), x=[y2[0],y3[0]], y=[y2[1], y3[1]])])

frames = [f1, f2, f3, f4]




# Create and add slider
steps = []
# for i in range(len(fig.data)):
for i, frame in enumerate(frames):
    # step = dict(
    #     method="restyle",
    #     args=["visible", [True] * (i+1) + [False] * (len(fig.data)-i-1)],
    #     name = "0"
    # )
    step = dict(
        method="animate",
        args=[[frame.name],{"frame": {"duration": 300, "redraw": False}, "mode": "immediate", "transition": {"duration": 300}}],
        label = i,
        name=frame.name
    )
# #     # step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)


sliders = [dict(
    active=0,
    currentvalue={"prefix": "Step: "},
    # pad={"t": len(fig.data)},
    transition={"duration": 300, "easing": "cubic-in-out"},
    steps=steps
)]


layout = dict(
    sliders=sliders,
    hovermode="closest",
    title=r'$\text{Euler Method for:    } y=e^t$',
    xaxis_title="Time (s)",
    yaxis_title="Position (m)",
    font=dict(
        # family="Courier New, monospace",
        size=18
        )

)

# Create figure
# fig = go.Figure(data=[go.Scatter(visible=True, name="Truth", x=x, y=y),go.Scatter(visible=False, name="Step 1", line=dict(color='red'), x=[y0[0],y1[0]], y=[y0[1], y1[1]]), go.Scatter(visible=False,name="Step 2", line=dict(color='purple'), x=[y1[0],y2[0]], y=[y1[1], y2[1]]), go.Scatter(visible=False,name="Step 3", line=dict(color='green'), x=[y2[0],y3[0]], y=[y2[1], y3[1]])],
fig = go.Figure(data=[go.Scatter(visible=True, name="Truth", x=x, y=y, line=dict(color='purple')), go.Scatter(visible=True, name="Truth", x=x, y=y, line=dict(color='purple'))],  
  frames=frames, 
  layout=layout)

fig.show()


fig.write_html("euler.html", include_mathjax='cdn')
