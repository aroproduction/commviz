import streamlit as st
import numpy as np

from core.signals import (
    rectangular_pulse,
    signum_signal,
    sinc_signal,
    triangular_wave,
    unit_impulse,
    unit_step,
    ramp,
    exponential,
    sinusoid,
)


def build_signal_ui(signal_type: str):
    """
    Reusable UI component for building signals.
    Returns a Signal object.
    """

    # Unit Impulse
    # -------------------------------
    if signal_type == "Unit Impulse":
        return unit_impulse()

    # Unit Step
    # -------------------------------
    elif signal_type == "Unit Step":
        col1, col2 = st.columns([1, 2])

        with col1:
            constant = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)

        return unit_step(constant)

    # Ramp
    # -------------------------------
    elif signal_type == "Ramp":
        return ramp()

    # Exponential
    # -------------------------------
    elif signal_type == "Exponential":
        col1, col2 = st.columns([1, 2])

        with col1:
            a = st.slider("Exponent (a)", -5.0, 5.0, 1.0, 0.1)

        return exponential(a)

    # Sinusoidal
    # -------------------------------
    elif signal_type == "Sinusoidal":
        col1, col2, col3 = st.columns(3)

        with col1:
            amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)

        with col2:
            frequency = st.slider("Frequency (Hz)", 0.1, 10.0, 1.0, 0.1)

        with col3:
            phase = st.slider("Phase (rad)", -np.pi, np.pi, 0.0, 0.1)

        return sinusoid(amplitude, frequency, phase)

    # Sinc Signal
    # -------------------------------
    elif signal_type == "Sinc":
        col1 = st.columns(1)[0]
        with col1:
            amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        return sinc_signal(amplitude)

    # Signum Signal
    # -------------------------------
    elif signal_type == "Signum":
        return signum_signal()

    # Rectangular Pulse
    # -------------------------------
    elif signal_type == "Rectangular":
        col1, col2, col3 = st.columns(3)
        with col1:
            start = st.number_input("Start time", -5.0, 5.0, -1.0, 0.1)
        with col2:
            end = st.number_input("End time", -5.0, 5.0, 1.0, 0.1)
        with col3:
            amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        return rectangular_pulse(start, end, amplitude)

    # Triangular Wave
    # -------------------------------
    elif signal_type == "Triangular":
        col1, col2, col3 = st.columns(3)
        with col1:
            start = st.number_input("Start time", -5.0, 5.0, 0.0, 0.1)
        with col2:
            end = st.number_input("End time", -5.0, 5.0, 1.0, 0.1)
        with col3:
            amplitude = st.slider("Amplitude", 0.1, 5.0, 1.0, 0.1)
        return triangular_wave(start, end, amplitude)

    # Fallback (safety)
    # -------------------------------
    else:
        st.error("Unknown signal type")
        return None
