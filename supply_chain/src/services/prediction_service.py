from flask import jsonify
import joblib
import pandas as pd

from exceptions.app_exception import AppException



def predictPrice(data):
    try:
        # Load the model
        model = joblib.load('src/resources/pkl/xgb_price_model.pkl')
        # Example of columns in the order used during training
        columns = ['Quantite', 'ProductCategory', 'Brand', 'Shop', 'Year', 'Month', 'ProductionDuration', 'NbMaterials']
        df_input = pd.DataFrame([data], columns=columns)
        prediction = model.predict(df_input)
        return round(float(prediction[0]), 2)
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

