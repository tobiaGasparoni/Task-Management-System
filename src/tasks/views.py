from src.db import execute_and_fetch_query, execute_query
from src.middleware.token_required import token_required
from src.tasks.queries import get_create_task_query, get_delete_task_query, get_task_detail_query, get_task_list_query, get_update_task_query
from . import tasks_blueprint
from flask import request

from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres", echo=True)

@tasks_blueprint.get('/')
def index():
    return {'message': 'Welcome to the task management section of the platform!'}

@tasks_blueprint.post('/')
@token_required
def create_task(user):
    data = request.json
    
    user_fk = user['user_pk']
    title = data['title']
    description = data['description']

    insert_query, insert_params = get_create_task_query(title, description, user_fk)

    execute_query(insert_query, insert_params)

    return {
        'success': True
    }

@tasks_blueprint.get('/list')
@token_required
def list_tasks(user):
    user_fk = user['user_pk']

    select_query, select_params = get_task_list_query(user_fk)

    result = execute_and_fetch_query(select_query, select_params)

    return result

@tasks_blueprint.get('/<int:task_pk>')
@token_required
def task_detail(user, task_pk):
    select_query, select_params = get_task_detail_query(task_pk)

    result = execute_query(select_query, select_params)

    return result[0]

@tasks_blueprint.put('/<int:task_pk>')
@token_required
def update_task(user, task_pk):
    data = request.json

    title = data['title'],
    description = data['description'],
    status = data['status'],
    deleted = data['deleted']

    update_query, update_params = get_update_task_query(task_pk, title, description, status, deleted)

    execute_query(update_query, update_params)
    
    return {
        'success': True
    }

@tasks_blueprint.delete('/<int:task_pk>')
@token_required
def delete_task(user, task_pk):
    delete_query, delete_param = get_delete_task_query(task_pk)

    execute_query(delete_query, delete_param)

    return {
        'success': True
    }
