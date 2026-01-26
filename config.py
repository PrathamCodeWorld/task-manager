import os

class Config:
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = "postgresql://task_user:task_pass@localhost:5432/task_manager"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt-secret"
