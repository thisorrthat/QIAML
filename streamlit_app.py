import streamlit as st
from PIL import Image

import tensorflow as tf
import numpy as np

from model import loadmodel


st.title("QIAML Test Results")

file = st.file_uploader("Upload the image that you are wanting to classify here, either browse or drag ", type=("jpg"))




if file: 
    img = Image.open(file)
    st.title("Image Selected")
    resized_image = img.resize((200, 200))
    st.image(resized_image)
    st.title("Predicted Result")
    predictions = loadmodel(file)
    st.write(predictions)

