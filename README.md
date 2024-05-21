# Task-Management-System

## Run Locally

`docker-compose up`

If you wish to inspect the db in DBeaver, or any GUI to manage a DB, you can use the following settings:

Host: localhost
Port: 5432
Username: postgres
Password: postgres

To restart the platform: 

1. Quit the terminal with ctrl + c.
2. Run `./manager.sh clean`. It will delete the containers and the python image.
3. Re-run `docker-compose up`.

## Integration tests

Integration tests are also run through docker-compose. Just execute `./manager.sh integration-tests`.

## Unit Test Setup

pyenv global 3.11.6
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


## Notes for initial local development

To spin up a docker instance of postgres:

`docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres`
