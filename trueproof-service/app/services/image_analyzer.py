import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

model = load_model("models/fake_cnn_model.h5")

def analyze_image(file_bytes):
    img = Image.open(io.BytesIO(file_bytes)).resize((224, 224)).convert("RGB")
    arr = np.array(img) / 255.0
    arr = arr.reshape((1, 224, 224, 3))
    prediction = model.predict(arr)[0][0]
    return float(prediction)