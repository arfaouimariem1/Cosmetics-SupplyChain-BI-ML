import json
from flask import jsonify
import joblib
import pandas as pd

from exceptions.app_exception import AppException

import tensorflow as tf

import numpy as np
from PIL import Image
import io


def predictCartonDamage(image_bytes):
    try:
        print("📷 Lancement prédiction avec modèle CNN")
        model = tf.keras.models.load_model("src/resources/model/cnn_damage_detector.h5")

        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image = image.resize((64, 64))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)[0][0]
        return "damaged" if prediction >= 0.5 else "not damaged"

    except Exception as e:
        print("❌ Erreur lors de la prédiction CNN :", str(e))
        raise AppException("Error during image prediction", str(e), 500)



def predictPrice(data):
    try:
        # Charger le modèle
        model = joblib.load('src/resources/pkl/best_price_model.pkl')

        # Charger le mapping
        with open('src/resources/pkl/encoders_mapping.json', 'r') as f:
            encoders = json.load(f)

        # Encoder les champs texte si besoin
        for col in ["Brand", "ProductCategory", "Shop"]:
            if isinstance(data[col], str):
                if data[col] in encoders[col]:
                    data[col] = encoders[col][data[col]]
                else:
                    raise AppException("Encoding error", f"Unknown {col}: {data[col]}", 400)

        # Assurer que Year et Month sont des entiers
        data["Year"] = int(data["Year"])
        data["Month"] = int(data["Month"])

        # Créer DataFrame avec colonnes bien ordonnées
        columns = ['ProductCategory', 'Brand', 'Shop', 'Year', 'Month', 'ProductionDuration', 'NbMaterials']
        df_input = pd.DataFrame([data], columns=columns)

        # Prédiction
        prediction = model.predict(df_input)
        return round(float(prediction[0]), 2)

    except AppException:
        raise
    except Exception as e:
        raise AppException("Error during Price prediction", str(e), 500)


def predictValidationDate(data):
   
    try:
         # 🔁 Chargement modèle
        features = joblib.load("src/resources/pkl/xgb_validity_features.pkl")
        pipeline = joblib.load("src/resources/pkl/xgb_validity_model.pkl")
        df = pd.DataFrame([data], columns=features)
        prediction = pipeline.predict(df)[0]
        return round(float(prediction), 2)
    except Exception as e:
        raise AppException("Error during Validation Date prediction", str(e), 500)

def predictDosage(data):
    
    try:
        # 🔁 Chargement des objets
        model = joblib.load("src/resources/pkl/xgb_model.pkl")
        encoders = joblib.load("src/resources/pkl/xgb_label_encoders.pkl")
        features = joblib.load("src/resources/pkl/xgb_features.pkl")
        df = pd.DataFrame([data], columns=features)

        # 🔤 Encodage
        for col in ["ProductCategory", "Brand", "Unit"]:
            df[col] = encoders[col].transform(df[col])

        # 🔮 Prédiction
        prediction = model.predict(df)[0]
        return  round(float(prediction), 2)

    except Exception as e:
        raise AppException("Error during Dosage prediction", str(e), 500)

