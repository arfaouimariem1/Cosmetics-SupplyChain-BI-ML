from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# 📍 Chemin vers le modèle .h5
MODEL_PATH = os.path.join("resources", "model", "cnn_damage_detector.h5")
model = tf.keras.models.load_model(MODEL_PATH)

@app.route("/predict/carton-damage", methods=["POST"])


def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    try:
        image_file = request.files['image']
        image = Image.open(io.BytesIO(image_file.read())).convert("RGB")
        image = image.resize((64, 64))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)[0][0]
        label = "damaged" if prediction >= 0.5 else "not damaged"

        return jsonify({"result": label})

    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
