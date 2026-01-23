import streamlit as st
import numpy as np
from core.signals import time_axis, unit_impulse, unit_step, ramp, sinusoid
from core.systems import linear_system, discrete_system
from ui.plots import plot_signal


def run_systems_module():
    st.subheader("What is a System?")
    st.markdown(
        "A system takes an input signal and produces an output. "
        "Use the sliders to modify the system parameters and observe the effect on the output in real-time."
    )

    # -----------------------
    # 1️⃣ Input Signal Settings
    # -----------------------
    st.markdown("### Input Signal")
    signal_type = st.selectbox(
        "Select Input Signal",
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal"],
        key="system_input_signal",
        label_visibility="collapsed",
    )

    # Time axis
    t_min, t_max = -5.0, 5.0
    t = time_axis(t_min, t_max)

    # Generate input signal
    if signal_type == "Unit Impulse":
        x = unit_impulse(t)
    elif signal_type == "Unit Step":
        x = unit_step(t)
    elif signal_type == "Ramp":
        x = ramp(t)
    elif signal_type == "Sinusoidal":
        amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (Hz)", 0.1, 5.0, 1.0, 0.1)
        phase = st.slider("Phase (rad)", -np.pi, np.pi, 0.0, 0.1)
        x = sinusoid(t, amplitude, frequency, phase)

    # -----------------------
    # 2️⃣ System Settings in Sidebar
    # -----------------------
    st.sidebar.markdown("### System Settings")
    system_type = st.sidebar.selectbox(
        "System Type",
        ["Linear Gain", "Simple Discrete System"],
        key="system_type",
        label_visibility="collapsed",
    )

    # System parameters
    if system_type == "Linear Gain":
        k = st.sidebar.slider("Gain (k)", 0.1, 5.0, 1.0, 0.1)
        y = linear_system(x, k)
    elif system_type == "Simple Discrete System":
        alpha = st.sidebar.slider("Alpha (feedback)", 0.0, 1.0, 0.5, 0.05)
        y = discrete_system(x, alpha)

    # -----------------------
    # 3️⃣ Side-by-side plots
    # -----------------------
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            plot_signal(t, x, title="Input Signal"), use_container_width=True
        )

    with col2:
        st.plotly_chart(
            plot_signal(t, y, title="Output Signal"), use_container_width=True
        )
