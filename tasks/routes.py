from flask_jwt_extended import jwt_required , get_jwt_identity
from flask import request
from app.auth.models import User
from tasks.models import Task
from app.extensions import db
from tasks import tasks_bp

@tasks_bp.route('',methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return({"message":"title is required"},400)
    
    task = Task(
        title = data['title'],
        description = data.get('description'),
        user_id = int(get_jwt_identity())
    )
    db.session.add(task)
    db.session.commit()

    return {
        'title_id': task.id,
        'title': task.title,
        'status': task.status
    },201


@tasks_bp.route("",methods=['GET'])
@jwt_required()
def get_my_task():
    user_id = int(get_jwt_identity())
    tasks = Task.query.filter_by(user_id=user_id).all()
    return [
        {
            'id': t.id,
            'title':t.title,
            'status':t.status
        }
        for t in tasks
    ]

@tasks_bp.route("/<int:task_id>",methods=['GET'])
@jwt_required()
def get_task_byID(task_id):
    task = Task.query.get_or_404(task_id)
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    if(user_id != task.user_id or user.role != 'admin'):
        return {"message":"forbidden"},403
    return {
        'id': title_id,
        'title':task.title,
        'status':task.status
    } 

@tasks_bp.route("/<int:task_id>",methods=['PUT'])
@jwt_required()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    if (task.user_id != user_id or user.role != 'admin'):
        return {"message":"forbidden"},403

    data = request.get_json()
    task.title = data.get('title',task.title)
    task.description = data.get('description',task.description)
    task.status = data.get('status',task.status)

    db.session.commit()
    return {
        'message': 'Task updated',
        'id': title_id,
        'title':task.title,
        'status':task.status
    }

@tasks_bp.route('/<int:task_id>',methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    task = Tasks.query.get_or_404(task_id)
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    if(user_id != task.user_id or user.role != 'admin'):
        return {"message": "forbidden"},403

    db.session.delete(task)
    db.session.commit()

    return {"message": "successfully deleted record"}    
