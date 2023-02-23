import streamlit as st
import subprocess

def open_terminal():
    subprocess.Popen('x-terminal-emulator')
    
if st.button('Open Terminal'):
    open_terminal()
