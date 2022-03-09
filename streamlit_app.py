import streamlit as st
import os
from PIL import Image

@st.cache()
def load_model():
	"""Retrieves the model for the test"""
	model = tf.keras.models.load_model('classifier BC')
	return model


st.title("QIAML")
st.title("Upload Test File Here")

file = st.file_uploader("Upload a image", type=("png", "jpg", "bmp"))
#if file: #is uploaded file
#	img = Image.open(file)
#	prediction = predict(img, model)
#	top_prediciton = prediciton

if file: 
	img = Image.open(file)


	st.title("Image Selected")
	resized_image = img.resize((200, 200))
	st.image(resized_image)
	st.title("Predicted Result")

