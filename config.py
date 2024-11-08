from utils.secrets_generator import generate_secret


class Config:
    SECRET_KEY = generate_secret()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False