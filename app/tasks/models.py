from app.extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__='tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(60), default='pending')
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
