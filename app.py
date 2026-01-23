import streamlit as st
from modules.impulse_response import run_impulse_response_module
from modules.signals import run_signals_module
from modules.basic_operations import run_basic_operations_module
from modules.system_properties import run_system_properties_module
from modules.systems import run_systems_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Communication Systems Viz")
st.sidebar.markdown("---")

signal_topic = st.sidebar.radio(
    "Signal Analysis",
    [
        "Signal Foundations",
        "Signal Operations",
        "Systems",
        "System Properties",
        "Impulse Respnose",
    ],
    key="signal_analysis",
)

if signal_topic == "Signal Foundations":
    run_signals_module()
elif signal_topic == "Signal Operations":
    run_basic_operations_module()
elif signal_topic == "Systems":
    run_systems_module()
elif signal_topic == "System Properties":
    run_system_properties_module()
elif signal_topic == "Impulse Respnose":
    run_impulse_response_module()
