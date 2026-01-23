import streamlit as st
import numpy as np

from core.signals import (
    time_axis,
    unit_impulse,
    unit_step,
    ramp,
    exponential,
    sinusoid,
)
from ui.plots import plot_signal


def run_signals_module():
    signal_mode = st.radio(
        "Signal Mode",
        ("Continuous", "Discrete"),
        index=0,  # default to Continuous
        horizontal=True,
    )

    # Time settings
    st.subheader("Time Settings")

    col1, col2 = st.columns(2)

    with col1:
        t_min = st.number_input("Start Time", value=-1.0, step=0.1, format="%.5f")

    with col2:
        t_max = st.number_input("End Time", value=1.0, step=0.1, format="%.5f")

    if t_min >= t_max:
        st.warning("Start time must be less than end time.")
        return

    if signal_mode == "Discrete":
        num_points = min(100, int(t_max - t_min) * 10)
        t = np.linspace(t_min, t_max, num_points)
    else:
        t = time_axis(t_min, t_max)

    # Signal selection
    signal_type = st.selectbox(
        "Select Signal",
        ["Unit Impulse", "Unit Step", "Ramp", "Exponential", "Sinusoidal"],
    )

    # Parameter controls
    if signal_type == "Unit Impulse":
        x = unit_impulse(t)

    elif signal_type == "Unit Step":
        x = unit_step(t)

    elif signal_type == "Ramp":
        x = ramp(t)

    elif signal_type == "Exponential":
        a = st.slider("Exponential Constant (a)", -5.0, 5.0, 1.0, 0.1)
        x = exponential(t, a)

    elif signal_type == "Sinusoidal":
        amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (Hz)", 0.1, 10.0, 1.0, 0.1)
        phase = st.slider("Phase (rad)", -np.pi, np.pi, 0.0, 0.1)
        x = sinusoid(t, amplitude, frequency, phase)

    # Plot
    fig = plot_signal(t, x, title=signal_type)
    st.plotly_chart(fig, width='stretch')
