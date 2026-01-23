import streamlit as st
import numpy as np
from core.signals import time_axis, unit_impulse, unit_step, ramp, sinusoid
from core.systems import linear_system, discrete_system
from core.system_properties import (
    linearity_test,
    time_invariance_test,
    causality_test,
    stability_test,
)
from ui.plots import plot_signal


def run_system_properties_module():
    st.subheader("2.2 System Properties")
    st.markdown("Toggle system properties to see their effect on output signals.")

    # -----------------------
    # Input signal
    # -----------------------
    t = time_axis(-5, 5)
    signal_type = st.selectbox(
        "Input Signal",
        ["Unit Impulse", "Unit Step", "Ramp", "Sinusoidal"],
        key="prop_input_signal",
        label_visibility="collapsed",
    )

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

    st.markdown("**Input Signal**")
    st.plotly_chart(plot_signal(t, x, title="Input Signal"), use_container_width=True)

    # -----------------------
    # System selection
    # -----------------------
    system_type = st.selectbox(
        "System Type",
        ["Linear Gain", "Simple Discrete System"],
        key="prop_system_type",
        label_visibility="collapsed",
    )

    if system_type == "Linear Gain":
        k = st.slider("Gain (k)", 0.1, 5.0, 1.0, 0.1)
        system_func = lambda inp: linear_system(inp, k)
    else:
        alpha = st.slider("Alpha (feedback)", 0.0, 1.0, 0.5, 0.05)
        system_func = lambda inp: discrete_system(inp, alpha)

    # -----------------------
    # Property toggles
    # -----------------------
    st.markdown("### System Properties")
    col1, col2 = st.columns(2)

    with col1:
        linearity = st.checkbox("Linearity", value=False)
        time_invariant = st.checkbox("Time Invariance", value=False)
    with col2:
        causality = st.checkbox("Causality", value=False)
        stability = st.checkbox("Stability", value=False)

    # -----------------------
    # Compute output based on properties
    # -----------------------
    y = system_func(x)  # default output

    # Linearity demo
    if linearity:
        x2 = x * 0.5
        y_combined, y_expected = linearity_test(x, x2, system_func)
        y = y_expected  # show expected linear output
        st.markdown("**Linearity Test Applied (scaled + added input)**")

    # Time-invariance demo
    if time_invariant:
        shift_idx = 10  # arbitrary index shift
        y_shifted, y_expected = time_invariance_test(x, system_func, shift_idx)
        y = y_expected
        st.markdown("**Time-Invariance Test Applied (shifted input)**")

    # Causality demo
    if causality:
        y = causality_test(x, system_func)
        st.markdown("**Causality Test Applied (future input blocked)**")

    # Stability demo
    if stability:
        y, is_stable = stability_test(x, system_func)
        st.markdown(
            f"**Stability Test Applied → System is {'Stable' if is_stable else 'Unstable'}**"
        )

    # -----------------------
    # Plot output
    # -----------------------
    st.markdown("**Output Signal**")
    st.plotly_chart(plot_signal(t, y, title="Output Signal"), use_container_width=True)
