import numpy as np
def grabImage (img):
    img = np.array(img)
    img = img/(255.0)
    img = img.tolist()
    return img