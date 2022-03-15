import streamlit as st
from PIL import Image
import numpy as np
from model import loadmodel, predict


st.title("QIAML Test Results")

file = st.file_uploader("Upload the image that you are wanting to classify here, either browse or drag ", type=("jpg"))
model = loadmodel()

class_names = ['High', 'Low', 'Medium']
if file: 
    img = Image.open(file)
    st.title("Image Selected")
    resized_image = img.resize((200, 200))
    st.image(resized_image)
    predictions = predict(img, model)
    predictions_label = np.argmax(predictions[0])
    label = class_names[predictions_label]
    st.title("Predicted Result")
    st.dataframe(predictions)
    

