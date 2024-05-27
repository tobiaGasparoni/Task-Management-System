from datetime import datetime, timedelta, timezone
from src.auth.hasher import Hasher
from src.auth.json_web_tokens import JWTProcessor
from . import auth_blueprint
from flask import request
from sqlalchemy import create_engine, text
from src.middleware.token_required import token_required
import redis


engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres", echo=True)


@auth_blueprint.route('/')
def index():
    return {'message': 'Welcome to the auth section of the platform!'}


@auth_blueprint.post('/')
def create_user():
    data = request.json

    hasher = Hasher()
    hashed_password = hasher.hash_password(data['password'])

    insert_query = '''INSERT INTO users (
            first_name, last_name, email, password
        ) VALUES
        (:first_name, :last_name, :email, :password)'''
    insert_params = {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'password': hashed_password
    }

    with engine.connect() as connection:
        connection.execute(text(insert_query), insert_params)
        connection.commit()

    return {
        'success': True
    }


@auth_blueprint.post('/login')
def login():
    data = request.json

    hasher = Hasher()
    hashed_password = hasher.hash_password(data['password'])

    select_params = {'email': data['email']}
    select_query = 'SELECT * FROM users WHERE email = :email;'

    with engine.connect() as connection:
        rows = connection.execute(text(select_query), select_params)

    for row in rows:
        user_data = row._asdict()

    if user_data is None:
        return {
            'message': 'Incorrect credentials: username and password are incorrect.'
        }

    if user_data['password'] == hashed_password:
        jwt_processor = JWTProcessor()
        payload = {
            'exp': datetime.now(tz=timezone.utc) + timedelta(days=1),
            'user_id': user_data['user_pk']
        }
        json_web_token = jwt_processor.encode(payload)
        return {
            'jwt': json_web_token
        }
    else:
        pass


@auth_blueprint.get('/logout')
@token_required
def logout(user):
    jwt = user['jwt']

    r = redis.Redis(host='redis', port=6379, decode_responses=True)

    r.set(jwt, 1)

    return {
        'success': True
    }


@auth_blueprint.put('/')
@token_required
def update_user(user):
    user_pk = user['user_pk']

    update_query = '''UPDATE users
        SET first_name = :first_name,
            last_name = :last_name,
            email = :email,
            updated_at = NOW()
        WHERE user_pk = :user_pk;'''
    data = request.json
    update_params = {
        'user_pk': user_pk,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email']
    }

    with engine.connect() as connection:
        connection.execute(text(update_query), update_params)
        connection.commit()
    
    return {
        'success': True
    }


@auth_blueprint.delete('/')
def delete_user():
    pass
