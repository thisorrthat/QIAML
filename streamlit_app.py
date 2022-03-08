import streamlit as st
import os

@st.cache()
def load_model
	"""Retrieves the model for the test"""
	model = tf.keras.models.load_model('classifier BC')
	return model

st.title('QIAML')
st.header('Upload Test File Here')
file_bytes = st.file_uploader("Upload a file", type=("png", "jpg", "bmp"))
