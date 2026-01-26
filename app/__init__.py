from flask import Flask
from app.extensions import db,jwt
from config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    #from app.auth.routes import auth_bp
    #app.register.bluerint(auth_bp, url_prefix='/auth')

    return app
