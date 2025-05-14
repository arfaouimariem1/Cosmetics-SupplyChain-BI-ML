import os
import traceback
from typing import Tuple
from flask import Flask, jsonify, Response
from flask_cors import CORS
from exceptions.app_exception import AppException
from services.api_resource_service import ApiResourceService
from services.bcrypt_service import bcrypt
from services.user_service import db

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/supplychain'

db.init_app(app)
bcrypt.init_app(app)

# CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*")
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

# Gestion des erreurs
@app.errorhandler(Exception)
def internal_server_error(error) -> Tuple[Response, int]:
    app.logger.error(traceback.format_exc())
    return jsonify({'message': 'Internal error', 'description': str(error)}), 500

@app.errorhandler(AppException)
def app_error(error: AppException) -> Tuple[Response, int]:
    app.logger.error(traceback.format_exc())
    return jsonify({'message': error.message, 'description': error.description}), error.status_code

# Enregistrement des routes
print("🔧 Initialisation des routes...")
ApiResourceService(app).add_resources()

# Affichage des routes
print("✅ ROUTES DISPONIBLES :")
print(app.url_map)

# Démarrage
if __name__ == "__main__":
    app.run(debug=True)
