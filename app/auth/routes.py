from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.auth.models import User
from app.auth.services import register_user

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def registration():
    data = request.json
    user = register_user(data['email'],data['password'])

    if not user:
        return jsonify({'message':'User already exist'}), 400

    return jsonify({'message':'User registered Successfully'}), 201

@auth_bp.route('/login',methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid Credentials'}), 401

    token = create_access_token(identity = str(user.id))     
    return jsonify(access_token=token)

@auth_bp.route('/me',methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return(
            {
                "id" : user.id,
                "email" : user.email,
                "role" : user.role
            }
        )



