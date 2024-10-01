from urllib.request import urlopen
import requests
import pytest
from sqlalchemy import create_engine, text
import redis


class TestAuth:

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

    def execute_query(self, query):
        with self.DB_ENGINE.connect() as connection:
            connection.execute(text(query))
            connection.commit()


    def execute_and_fetch_query(self, query):
        with self.DB_ENGINE.connect() as connection:
            rows = connection.execute(text(query))
            connection.commit()

        result = []
        for row in rows:
            result.append(row._asdict())

        return result


    def empty_database(self):
        self.execute_query('DELETE FROM users;')


    def create_user(self):
        new_user = {
            "first_name": "Robert",
            "last_name": "Martinez",
            "email": "robert.martinez@gmail.com",
            "password": "password123again"
        }

        response = requests.post(self.AUTH_URL, json=new_user)
    
        data = response.json()
        
        assert data == { "success": True }

    #####
    # Tests
    #####

    def test_hello(self):
        expected = {'message':'Welcome to the auth section of the platform!'}

        response = requests.get(self.AUTH_URL)
        data = response.json()
        
        assert data == expected

        self.empty_database()


    def test_create_user(self):
        self.create_user()

        query = """SELECT * FROM users WHERE email='robert.martinez@gmail.com'"""
        users = self.execute_and_fetch_query(query)

        assert len(users) == 1
        added_user = users[0]
        assert added_user['first_name'] == 'Robert'
        assert added_user['last_name'] == 'Martinez'
        assert added_user['password'] != 'password123again'

        self.empty_database()


    def test_login(self):
        self.create_user()

        login_credentials = {
            "email": "robert.martinez@gmail.com",
            "password": "password123again"
        }

        response = requests.post(self.AUTH_URL + '/login', json=login_credentials)
        data = response.json()

        json_web_token = data['jwt']
        assert json_web_token is not None
        assert len(json_web_token.split('.')) == 3

        self.empty_database()


    # def test_update_user(self):
    #     self.create_user()

    #     new_user_data = {
    #         "first_name": "Tobia",
    #         "last_name": "Martinez",
    #         "email": "tobia.martinez@gmail.com",
    #     }

    #     response = requests.put(self.AUTH_URL, json=new_user_data, headers={'Authorization': self.jwt})
    #     assert response.json() == { "success": True }

    #     query = """SELECT * FROM users WHERE email='tobia.martinez@gmail.com';"""
    #     users = self.execute_and_fetch_query(query)

    #     assert len(users) == 1
    #     added_user = users[0]
    #     assert added_user['first_name'] == 'Tobia'
    #     assert added_user['last_name'] == 'Martinez'

    #     self.empty_database()


    def test_logout_user(self):
        self.create_user()

        # Login logic from test_login()

        login_credentials = {
            "email": "robert.martinez@gmail.com",
            "password": "password123again"
        }

        response = requests.post(self.AUTH_URL + '/login', json=login_credentials)
        data = response.json()

        json_web_token = data['jwt']
        assert json_web_token is not None
        assert len(json_web_token.split('.')) == 3

        # Logout logic

        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        assert r.get(json_web_token) is None

        response = requests.get(self.AUTH_URL + '/logout', headers={'Authorization': json_web_token})
        assert response.json() == { "success": True }

        cache_response = r.get(json_web_token)
        assert int(cache_response) == 1

        self.empty_database()
