import streamlit as st
from modules.signals import run_signals_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Comm. Systems Visualizer")
st.sidebar.markdown("---")

signal_topic = st.sidebar.radio(
    "Signal Analysis",
    [
        "Signal Foundations",
        "Signal Operations",
        "Systems",
        "System Properties",
        "Impulse Respnose",
        "Convolution",
    ],
    key="signal_analysis",
)

if signal_topic == "Signal Foundations":
    run_signals_module()
