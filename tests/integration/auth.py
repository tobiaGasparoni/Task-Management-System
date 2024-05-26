from urllib.request import urlopen
import requests
import pytest
from sqlalchemy import create_engine, text


USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'postgres'

DB_ENGINE = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

AUTH_URL = 'http://localhost:8000/auth'

#####
# Utils
#####

def execute_query(query):
    with DB_ENGINE.connect() as connection:
        connection.execute(text(query))
        connection.commit()


def execute_and_fetch_query(query):
    with DB_ENGINE.connect() as connection:
        rows = connection.execute(text(query))
        connection.commit()

    result = []
    for row in rows:
        result.append(row._asdict())

    return result


def empty_database():
    execute_query('DELETE FROM users;')


def create_user():
    print('Executing create_user fixture')
    new_user = {
        "first_name": "Robert",
        "last_name": "Martinez",
        "email": "robert.martinez@gmail.com",
        "password": "password123again"
    }

    return requests.post(AUTH_URL, json=new_user)

#####
# Tests
#####

def test_hello():
    expected = {'message':'Welcome to the auth section of the platform!'}

    response = requests.get(AUTH_URL)
    data = response.json()
    
    assert expected == data


def test_create_user():
    expected = { "success": True }

    response = create_user()
    data = response.json()
    
    assert expected == data

    query = """SELECT * FROM users WHERE email='robert.martinez@gmail.com'"""
    users = execute_and_fetch_query(query)

    assert len(users) == 1
    added_user = users[0]
    assert added_user['first_name'] == 'Robert'
    assert added_user['last_name'] == 'Martinez'
    assert added_user['password'] != 'password123again'

    empty_database()


def test_login():
    assert create_user().json() == { "success": True }

    login_credentials = {
        "email": "robert.martinez@gmail.com",
        "password": "password123again"
    }

    response = requests.post(AUTH_URL + '/login', json=login_credentials)
    data = response.json()

    json_web_token = data['jwt']
    assert json_web_token is not None
    assert len(json_web_token.split('.')) == 3

    empty_database()


def test_update_user():

    assert create_user().json() == { "success": True }

    login_credentials = {
        "email": "robert.martinez@gmail.com",
        "password": "password123again"
    }

    response = requests.post(AUTH_URL + '/login', json=login_credentials)
    json_web_token = response.json()['jwt']

    new_user_data = {
        "first_name": "Tobia",
        "last_name": "Martinez",
        "email": "tobia.martinez@gmail.com",
    }

    response = requests.put(AUTH_URL, json=new_user_data, headers={'Authorization': json_web_token})
    assert response.json() == { "success": True }

    query = """SELECT * FROM users WHERE email='tobia.martinez@gmail.com';"""
    users = execute_and_fetch_query(query)

    assert len(users) == 1
    added_user = users[0]
    assert added_user['first_name'] == 'Tobia'
    assert added_user['last_name'] == 'Martinez'

    empty_database()
