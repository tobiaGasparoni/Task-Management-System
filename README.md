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

This endpoint creates a user in the database.

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
    "first_name": "FirstName",
    "last_name": "LastName",
    "email": "firstname.lastname@gmail.com",
    "password": "password12345"
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

This endpoint logs you into the system to access your tasks. The response is a JSON Web Token for you to use in every `/tasks` endpoint. This token will last 1 day.

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
    "email": "firstname.lastname@gmail.com",
    "password": "password12345"
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

This endpoint modifies the first name, last name, and email of a user.

URL:
```
PUT /auth
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
    "first_name": "NewName",
    "last_name": "NewLastName",
    "email": "newname.newlastname@gmail.com"
}
```

Response:
```
{
    "success": True
}
```

### Tasks

#### Create a task



#### List your tasks



#### See a task's detail



#### Update a task



#### Delete a task

