import tensorflow as tf
from grabImage import grabImage
def compair(img):
    grabImage(img) 
    model = tf.keras.models.load_model('classifier 3_split_final')
    classification = model.predict(img)
    return classification
