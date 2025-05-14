from flask import Flask
from services.user_service import db
from services.bcrypt_service import bcrypt
from services.user_service import create_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/supplychain'
app.config['SECRET_KEY'] = 'my_secret'

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    # ✅ À adapter si besoin :
    create_user(
        email="SamarAmri@esprit.tn",
        password="prod123",
        fullname="Samar Amri",
        role="production"
    )

with app.app_context():
    create_user(
        email="Fatma@esprit.tn",
        password="vente123",
        fullname="Fatma Ben Rabii",
        role="vente"
    )

