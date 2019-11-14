import numpy as np
import plotly.graph_objects as go

n = 100

x = np.linspace(-1, 3, n)
y = np.exp(x)
y0 = (0, 1)
y1 = (1, 2)
y2 = (2, 4)
y3 = (3, 8) 

# Create figure
fig = go.Figure()

# Add traces, one for each slider step
# for step in np.arange(0, 5, 0.1):
#     fig.add_trace(
#         go.Scatter(
#             visible=False,
#             line=dict(color="#00CED1", width=6),
#             name="𝜈 = " + str(step),
#             x=np.arange(0, 10, 0.01),
#             y=np.sin(step * np.arange(0, 10, 0.01))))

fig.add_trace(go.Scatter(visible=True, name="Truth", x=x, y=y))
fig.add_trace(go.Scatter(visible=False, name="Step 1", line=dict(color='red'), x=[y0[0],y1[0]], y=[y0[1], y1[1]]))
fig.add_trace(go.Scatter(visible=False, name="Step 2", line=dict(color='purple'), x=[y1[0],y2[0]], y=[y1[1], y2[1]]))
fig.add_trace(go.Scatter(visible=False, name="Step 3", line=dict(color='green'), x=[y2[0],y3[0]], y=[y2[1], y3[1]]))

# Make 10th trace visible
# fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [True] * (i+1) + [False] * (len(fig.data)-i-1)],
        name = "0"
    )
    # step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Step: "},
    pad={"t": len(fig.data)},
    transition={"duration": 300, "easing": "cubic-in-out"},
    steps=steps
)]

fig.update_layout(
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

# fig.show()









# fig = go.Figure(
#     data=[go.Scatter(x=x, y=y,
#                      mode="lines",
#                      line=dict(width=2, color="blue")),
#           go.Scatter(x=x, y=y,
#                      mode="lines",
#                      line=dict(width=2, color="blue"))],
#     layout=go.Layout(
#         xaxis=dict(range=[-1, 3], autorange=False, zeroline=False),
#         yaxis=dict(range=[0, 9], autorange=False, zeroline=False),
#         title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
#         updatemenus=[dict(type="buttons",
#                           buttons=[dict(label="Play",
#                                         method="animate",
#                                         args=[None])])]),
#     # frames=[go.Frame(
#     #     data=[go.Scatter(
#     #         x=[x[k], 1, None,x[k], 2 ],
#     #         y=[y[k], 2, None, y[k], 3],
#     #         mode="lines",
#     #         marker=dict(color="red", size=10))])
#     #         for k in range(n)]
#     frames=[go.Frame(data=[go.Scatter(x=[1, 1.5], y=[1, 2], mode='lines', line=dict(color='red'), name="yup")]),
#             go.Frame(data=[go.Scatter(x=[1, 4, None, 2, 2], y=[1, 4, None, 3, 5], mode='lines', line=dict(color='red'))]),
#             go.Frame(data=[go.Scatter(x=[1, 4, None, 2, 2], y=[1, 4, None, 4, 6], mode='lines', line=dict(color='red'))])]


# )

fig.write_html("euler.html", include_mathjax='cdn')
