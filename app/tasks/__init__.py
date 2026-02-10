from flask import Blueprint

tasks_bp = Blueprint("tasks",__name__)

from app.tasks import routes

from app.tasks.models import Task