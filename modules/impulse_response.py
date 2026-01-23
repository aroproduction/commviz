import streamlit as st
import numpy as np
from core.signals import time_axis, unit_impulse, sinusoid
from core.systems import linear_system, discrete_system
from core.impulse_response import (
    impulse_response_linear,
    impulse_response_exponential,
    impulse_response_ramp,
)
from ui.plots import plot_signal


def run_impulse_response_module():
    st.subheader("2.3 Impulse Response")
    st.markdown("Observe how different impulse responses characterize a system.")

    # -----------------------
    # Input signal
    # -----------------------
    t = time_axis(-5, 5, dt=0.1)  # finer resolution
    signal_type = st.selectbox(
        "Input Signal",
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal"],
        key="imp_input_signal",
        label_visibility="collapsed",
    )

    if signal_type == "Unit Impulse":
        x = unit_impulse(t)
    elif signal_type == "Unit Step":
        x = np.heaviside(t, 1.0)
    elif signal_type == "Ramp":
        x = t
    elif signal_type == "Sinusoidal":
        amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (Hz)", 0.1, 5.0, 1.0, 0.1)
        phase = st.slider("Phase (rad)", -np.pi, np.pi, 0.0, 0.1)
        x = amplitude * np.sin(2 * np.pi * frequency * t + phase)

    # -----------------------
    # System selection
    # -----------------------
    st.sidebar.markdown("### System Settings")
    system_type = st.sidebar.selectbox(
        "System Type",
        ["Linear Gain", "Simple Discrete System"],
        key="imp_system_type",
        label_visibility="collapsed",
    )

    if system_type == "Linear Gain":
        k = st.sidebar.slider("Gain (k)", 0.1, 5.0, 1.0, 0.1)
        system_func = lambda inp: linear_system(inp, k)
    else:
        alpha = st.sidebar.slider("Alpha (feedback)", 0.0, 1.0, 0.5, 0.05)
        system_func = lambda inp: discrete_system(inp, alpha)

    # -----------------------
    # Impulse Response selection
    # -----------------------
    st.markdown("### Impulse Response")
    h_type = st.selectbox(
        "Select Impulse Response",
        ["Delta (Linear)", "Exponential Decay", "Ramp"],
        key="impulse_response_type",
        label_visibility="collapsed",
    )

    length = len(t)
    if h_type == "Delta (Linear)":
        h = impulse_response_linear(length)
    elif h_type == "Exponential Decay":
        alpha = st.slider("Decay factor (alpha)", 0.1, 1.0, 0.5, 0.05)
        h = impulse_response_exponential(length, alpha)
    elif h_type == "Ramp":
        h = impulse_response_ramp(length)

    # -----------------------
    # Compute output
    # -----------------------
    # Convolution (continuous simplified)
    dt = t[1] - t[0]
    y = np.convolve(x, h, mode="same") * dt

    # -----------------------
    # Side-by-side visualization
    # -----------------------
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Input Signal**")
        st.plotly_chart(
            plot_signal(t, x, title="Input Signal"), use_container_width=True
        )

    with col2:
        st.markdown("**Output Signal (after Impulse Response)**")
        st.plotly_chart(
            plot_signal(t, y, title=f"Output: {h_type}"), use_container_width=True
        )

    # Optional: visualize impulse response
    st.markdown("**Impulse Response**")
    st.plotly_chart(
        plot_signal(t, h, title=f"Impulse Response: {h_type}"), use_container_width=True
    )
