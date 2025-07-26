import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

MODEL_PATH = "models/fake_cnn_model.h5"
model = load_model(MODEL_PATH)

def classify_image(image_path: str):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]
    verdict = "Likely Manipulated" if pred > 0.5 else "Authentic"
    return {
        "manipulation_score": float(pred),
        "verdict": verdict,
        "model": "FakeCNN-v1"
    }