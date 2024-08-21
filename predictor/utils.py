# predictions/utils.py
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np



def load_trained_model():
    model = load_model('predictor/model_epoch302.h5')
    return model


