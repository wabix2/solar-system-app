
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="3D Interactive Solar System", layout="wide")
st.title("🌞 3D Interactive Solar System")

# Planet data: [semi-major axis, semi-minor axis, size, speed, color]
planets = {
    "Mercury": [0.4, 0.38, 10, 0.04, 'grey'],
    "Venus": [0.7, 0.69, 15, 0.03, 'orange'],
    "Earth": [1.0, 0.99, 18, 0.02, 'blue'],
    "Mars": [1.5, 1.48, 12, 0.015, 'red'],
    "Jupiter": [2.2, 2.15, 25, 0.01, 'brown'],
    "Saturn": [2.8, 2.7, 22, 0.008, 'gold'],
    "Uranus": [3.4, 3.35, 20, 0.006, 'lightblue'],
    "Neptune": [4.0, 3.95, 20, 0.005, 'darkblue']
}

frames = []
num_frames = 200

# Precompute planet positions
for i in range(num_frames):
    data = []
    for planet, info in planets.items():
        a, b, size, speed, color = info
        x = a * np.cos(speed * i * 2*np.pi)
        y = b * np.sin(speed * i * 2*np.pi)
        z = 0
        data.append(go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='markers',
            marker=dict(size=size, color=color),
            name=planet,
            showlegend=False
        ))
    frames.append(go.Frame(data=data, name=str(i)))

# Initial positions (frame 0)
initial_data = frames[0].data

# Sun in the center
sun = go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='markers',
    marker=dict(size=35, color='yellow'),
    name='Sun'
)

fig = go.Figure(
    data=[sun]+list(initial_data),
    layout=go.Layout(
        scene=dict(
            xaxis=dict(showbackground=False),
            yaxis=dict(showbackground=False),
            zaxis=dict(showbackground=False),
            aspectmode='data'
        ),
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(label='Play',
                          method='animate',
                          args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)])]
        )]
    ),
    frames=frames
)

st.plotly_chart(fig, use_container_width=True)

