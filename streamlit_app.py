import streamlit as st
import os
st.title('QIAML')
st.header('Upload Test File Here')
file_bytes = st.file_uploader("Upload a file", type=("png", "jpg", "bmp"))

