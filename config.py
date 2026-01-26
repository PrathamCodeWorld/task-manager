import os

class Config:
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///task_manager.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt-secret"
