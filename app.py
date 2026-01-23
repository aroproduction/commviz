import streamlit as st
from modules.signals import run_signals_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Communication Systems Viz")
st.sidebar.markdown("---")

topic = st.sidebar.selectbox("Select Topic", ["Signal Foundations"])

if topic == "Signal Foundations":
    run_signals_module()
