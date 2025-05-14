from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)

    
#la partie securisation de passwor que j'ajoute 

from services.bcrypt_service import bcrypt
from services.user_service import db, User

def create_user(email, password, fullname, role):
    # 🔒 Chiffrer le mot de passe
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # 📄 Créer l'utilisateur
    new_user = User(
        email=email,
        password=hashed_password,
        fullname=fullname,
        role=role
    )

    # 💾 Enregistrer dans la base
    db.session.add(new_user)
    db.session.commit()

    print(f"✅ Utilisateur {email} créé avec succès.")
