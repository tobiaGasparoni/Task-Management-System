from functools import wraps

from flask import request

from src.auth.json_web_tokens import JWTProcessor
from sqlalchemy import create_engine, text

import redis

engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres", echo=True)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        jwt = request.headers['Authorization']
        jwt_processor = JWTProcessor()

        payload = jwt_processor.decode(jwt)

        select_params = {
            'user_pk': payload['user_id']
        }

        r = redis.Redis(host='redis', port=6379, decode_responses=True)
        if r.get(jwt):
            raise Exception('Unauthorized')

        select_query = 'SELECT * FROM users WHERE user_pk = :user_pk;'

        with engine.connect() as connection:
            rows = connection.execute(text(select_query), select_params)

        user = None
        for row in rows:
            user = row._asdict()
        if user is not None:
            user['jwt'] = jwt
            return f(user, *args, **kwargs)
        else:
            raise Exception('Unauthorized')
    return decorated