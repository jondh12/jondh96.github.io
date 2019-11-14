import numpy as np
import plotly.graph_objects as go

n = 100
h = 1.0
x = np.linspace(-1, 5, n)
y = np.exp(x)


def funct(t, y):
    return y


def runge(h, yn, t):
    k1 = funct(t, yn)
    k2 = funct(t + h/2.0, yn + k1/2.0)
    k3 = funct(t+h/2.0, yn+k2/2.0)
    k4 = funct(t+h, yn+k3)
    print("K1 = {}\nK2 = {}\nK3 = {}\nK4 = {}\n".format(k1, k2, k3, k4))


    yn1 = yn + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return yn1
it = (0, 1)
it0 = (1, runge(h, 1, 0))
it1 = (2, runge(h, it0[1], 1))
it2 = (3, runge(h, it1[1], 2))
print(it0, it1, it2)

# p_1 = (.5, 1+ h*1)
# p_2 = (.5, 1+ h*1.5/2)
# p_3 = (1, 1+ h*1.75/2)
# p_4 = 0


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
# fig.add_trace(go.Scatter(visible=False, name="K1", line=dict(color='red'), x=[k[0][0]], y=[k[0][1]]))
# for index in range(3):
#     prev_point = k[index -1]
#     point = k[index]
#     fig.add_trace(go.Scatter(visible=False, name="K{}".format(index), line=dict(color='red'), x=[prev_point[0], point[0]], y=[prev_point[1], point[1]]))



# fig.add_trace(go.Scatter(visible=False, name="I1", line=dict(color='red'), x=[it[0], it0[0]], y=[it[1], it0[1]]))
# fig.add_trace(go.Scatter(visible=False, name="I2", line=dict(color='purple'), x=[it0[0],it1[0]], y=[it0[1], it1[1]]))
# fig.add_trace(go.Scatter(visible=False, name="I3", line=dict(color='green'), x=[it1[0], it2[0]], y=[it1[1], it2[1]]))

fig.add_trace(go.Scatter(visible=False, name="Step 1", line=dict(color='red'), x=[it[0], it0[0]], y=[it[1], it0[1]]))
fig.add_trace(go.Scatter(visible=False, name="Step 2", line=dict(color='purple'), x=[it0[0],it1[0]], y=[it0[1], it1[1]]))
fig.add_trace(go.Scatter(visible=False, name="Step 3", line=dict(color='green'), x=[it1[0], it2[0]], y=[it1[1], it2[1]]))

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
    title="Runge Kutta Method",
    xaxis_title="Time (s)",
    yaxis_title="Position(m)",
    font=dict(
        family="Courier New, monospace",
        size=18,
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

fig.write_html("runge.html")
