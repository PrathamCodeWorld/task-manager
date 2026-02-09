from flask_jwt_extended import get_jwt_identity, jwt_required
from app.auth.models import User
from functools import wraps

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            user = User.query.get(get_jwt_identity())
            if(role != user.role):
                return(
                    {"message":"forbidden Access"},403
                )
            return fn(*args,**kwargs)
        return decorator        
    return wrapper



'''
    @role_decorator("admin")
    def task_assign():
        ...
'''