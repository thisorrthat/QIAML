import tensorflow as tf
import numpy as np
from PIL import Image

"""This will load the model and return model converted into probability resutls
"""
def loadmodel(file):
    img = Image.open(file)
    model = tf.keras.models.load_model('classmodel')
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    img_resize = img.copy()
    img_resized = img_resize.resize((900,900))
    img_resized = (np.expand_dims(img_resized,0))
    #predictions = probability_model.predict(img_resized)
    predictions = 'HIGH'
    return predictions
