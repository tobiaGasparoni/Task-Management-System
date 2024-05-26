# Task-Management-System

## Index

1. Run Locally
2. Integration Tests
3. Unit Tests Setup
4. API Guide
   1. Authentication
      1. Create a user
      2. Login
      3. Update user
   2. Tasks
      1. Create a task
      2. List your tasks
      3. See a task's detail
      4. Update a task
      5. Delete a task

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

---

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

---

#### Create a task

This endpoint creates a task for the logged in user.

URL:
```
POST /tasks
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
    "title": "postman title",
    "description": "postman description"
}
```

Response:
```
{
    "success": True
}
```

---

#### List your tasks

This endpoint returns all the tasks related to the logged in user.

URL:
```
GET /tasks/list
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
{}
```

Response:
```
[
    {
        "created_at": "Sat, 18 May 2024 13:56:02 GMT",
        "status": "TO DO",
        "task_pk": 3,
        "title": "title1",
        "updated_at": "Sat, 18 May 2024 19:54:45 GMT"
    },
    {
        "created_at": "Sat, 18 May 2024 13:56:02 GMT",
        "status": "TO DO",
        "task_pk": 4,
        "title": "title2",
        "updated_at": "Sat, 18 May 2024 19:54:45 GMT"
    }
]
```

---

#### See a task's detail

This endpoint returns the detail of the task specified in the <task_id> parameter.

URL:
```
GET /tasks/<task_id>
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
{}
```

Response:
```
{
    "created_at": "Sat, 18 May 2024 13:56:02 GMT",
    "deleted": 0,
    "description": "description1 updated",
    "status": "TO DO",
    "task_pk": 4,
    "title": "title1 updated",
    "updated_at": "Sat, 18 May 2024 19:54:45 GMT"
}
```

---

#### Update a task

This endpoint changes the details of the task specified in the <task_id> parameter.

URL:
```
PUT /tasks/<task_id>
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
    "deleted": 0,
    "description": "description1 updated",
    "status": "TO DO",
    "title": "title1 updated"
}
```

Response:
```
{
    "created_at": "Sat, 18 May 2024 13:56:02 GMT",
    "deleted": 0,
    "description": "description1 updated",
    "status": "TO DO",
    "task_pk": 4,
    "title": "title1 updated",
    "updated_at": "Sat, 18 May 2024 19:54:45 GMT"
}
```

---

#### Delete a task

This endpoint deletes the task specified in the <task_id> parameter.

URL:
```
DELETE /tasks/<task_id>
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
{}
```

Response:
```
{
    "success": True
}
```
