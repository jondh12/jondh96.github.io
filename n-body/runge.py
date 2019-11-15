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


# # Create figure
# fig = go.Figure()

# # Add traces, one for each slider step
# # for step in np.arange(0, 5, 0.1):
# #     fig.add_trace(
# #         go.Scatter(
# #             visible=False,
# #             line=dict(color="#00CED1", width=6),
# #             name="𝜈 = " + str(step),
# #             x=np.arange(0, 10, 0.01),
# #             y=np.sin(step * np.arange(0, 10, 0.01))))

# fig.add_trace(go.Scatter(visible=True, name="Truth", x=x, y=y))
# # fig.add_trace(go.Scatter(visible=False, name="K1", line=dict(color='red'), x=[k[0][0]], y=[k[0][1]]))
# # for index in range(3):
# #     prev_point = k[index -1]
# #     point = k[index]
# #     fig.add_trace(go.Scatter(visible=False, name="K{}".format(index), line=dict(color='red'), x=[prev_point[0], point[0]], y=[prev_point[1], point[1]]))



# # fig.add_trace(go.Scatter(visible=False, name="I1", line=dict(color='red'), x=[it[0], it0[0]], y=[it[1], it0[1]]))
# # fig.add_trace(go.Scatter(visible=False, name="I2", line=dict(color='purple'), x=[it0[0],it1[0]], y=[it0[1], it1[1]]))
# # fig.add_trace(go.Scatter(visible=False, name="I3", line=dict(color='green'), x=[it1[0], it2[0]], y=[it1[1], it2[1]]))

# fig.add_trace(go.Scatter(visible=False, name="Step 1", line=dict(color='red'), x=[it[0], it0[0]], y=[it[1], it0[1]]))
# fig.add_trace(go.Scatter(visible=False, name="Step 2", line=dict(color='purple'), x=[it0[0],it1[0]], y=[it0[1], it1[1]]))
# fig.add_trace(go.Scatter(visible=False, name="Step 3", line=dict(color='green'), x=[it1[0], it2[0]], y=[it1[1], it2[1]]))

# # Make 10th trace visible
# # fig.data[10].visible = True

# # Create and add slider
# steps = []
# for i in range(len(fig.data)):
#     step = dict(
#         method="restyle",
#         args=["visible", [True] * (i+1) + [False] * (len(fig.data)-i-1)],
#         name = "0"
#     )
#     # step["args"][1][i] = True  # Toggle i'th trace to "visible"
#     steps.append(step)

# sliders = [dict(
#     active=10,
#     currentvalue={"prefix": "Step: "},
#     pad={"t": len(fig.data)},
#     transition={"duration": 300, "easing": "cubic-in-out"},
#     steps=steps
# )]

# fig.update_layout(
#     sliders=sliders,
#     hovermode="closest",
#     title=r'$\text{Runge Kutta Method for:    } y=e^t$',
#     xaxis_title="Time (s)",
#     yaxis_title="Position(m)",
#     font=dict(
#         # family="Courier New, monospace",
#         size=18
#         )

# )


f1 = go.Frame(name ="f1", data=[go.Scatter(x=x, y=y, line=dict(color='purple'))])
f2 = go.Frame(name ="f2", data=[go.Scatter(visible=True, name="Step 1", line=dict(color='red'), x=[it[0], it0[0]], y=[it[1], it0[1]])])
f3 = go.Frame(name ="f3", data=[go.Scatter(visible=True,name="Step 2", line=dict(color='blue'), x=[it0[0],it1[0]], y=[it0[1], it1[1]])])
f4 = go.Frame(name ="f4", data=[go.Scatter(name="Step 3", line=dict(color='green'), x=[it1[0], it2[0]], y=[it1[1], it2[1]])])


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
fig = go.Figure(data=[go.Scatter(visible=True, x=x, y=y, line=dict(color='purple'), name="Truth"), go.Scatter(visible=True, name="Truth", x=x, y=y, line=dict(color='purple'))],  
  frames=frames, 
  layout=layout)

fig.show()

fig.write_html("runge.html", include_mathjax='cdn')
