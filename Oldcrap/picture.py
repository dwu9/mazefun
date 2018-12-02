import numpy as np
from PIL import Image


def image_to_array(filename):
    picture = Image.open(filename)
    nparray = np.asarray(picture, dtype = int)
    lines = nparray[:, :, 0]
    return lines
