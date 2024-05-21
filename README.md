# Task-Management-System

## Run Locally

`docker-compose up`

If you wish to inspect the db in DBeaver, or any GUI to manage a DB, you can use the following settings:

Host: `localhost`
Port: `5432`
Username: `postgres`
Password: `postgres`

To restart the platform: 

1. Quit the terminal with `ctrl + c`.
2. Run `./manager.sh clean`. It will delete the containers and the python image.
3. Re-run `docker-compose up`.

## Integration tests

Integration tests are also run through docker-compose. Just execute `./manager.sh integration-tests`.

## Unit Test Setup

```
pyenv global 3.11.6
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./manager.sh unit-tests
```

## API Guide

### Authentication

#### Create a user

URL:
```
POST /auth/signup
```

Headers: 
```
{
    "Content-Type": "application/json"
}
```

Request body:
```
{
    "first_name": "Robert",
    "last_name": "Martinez",
    "email": "robert.martinez@gmail.com",
    "password": "password123again"
}
```

Response:
```
{
    "success": True
}
```

---

#### Login

This 

URL:
```
POST /auth/login
```

Headers: 
```
{
    "Content-Type": "application/json"
}
```

Request body:
```
{
    "email": "tobia.martinez@gmail.com",
    "password": "password123again"
}
```

Response:
```
{
    "jwt": "xxxxx.yyyyy.zzzzz"
}
```

---

#### Update user

URL:
```
POST /auth/login
```

Headers: 
```
{
    "Content-Type": "application/json",
    "Authorization": "xxxxx.yyyyy.zzzzz"
}
```

Request body:
```
{
    "email": "tobia.martinez@gmail.com",
    "password": "password123again"
}
```

Response:
```
{
    "jwt": "xxxxx.yyyyy.zzzzz"
}
```

### Tasks

#### Create a task



#### List your tasks



#### See a task's detail



#### Update a task



#### Delete a task

