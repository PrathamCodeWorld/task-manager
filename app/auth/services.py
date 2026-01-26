from app.auth.models import User
from app.extensions import db

def register_user(email,password):
    if(User.query.filter_by(email=email).first()):
        return None

    user = User(email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user

