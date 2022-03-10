import streamlit as st
from PIL import Image
import numpy as np

Results = "HIGH"
st.title("QIAML Test Results")


file = st.file_uploader("Upload the image that you are wanting to classify here, either browse or drag ", type=("png", "jpg", "bmp"))


if file: 
    img = Image.open(file)
    predict = np.asarray(img)
    st.title("Image Selected")
    resized_image = img.resize((200, 200))
    st.image(resized_image)
    st.title("Predicted Result")
    st.write(Results)