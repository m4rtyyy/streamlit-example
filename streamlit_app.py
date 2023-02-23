import streamlit as st
import subprocess

def open_terminal():
    subprocess.Popen(['gnome-terminal'])
    
if st.button('Open Terminal'):
    open_terminal()
