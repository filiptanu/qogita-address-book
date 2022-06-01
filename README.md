# Qogita interview assignment

This repository contains implementation of the specification defined in [back-end-engineer-assessment.md](back-end-engineer-assessment.md).

## Requirements

- Docker
- Docker Compose

## Running the API

To run the API, run:

```
docker-compose run api
```

To run the integration tests, run:

```
docker-compose run postman
```
## Reference

TODO (filiptanu): Maybe remove this section in the future

This project has been generated using `django-admin`. You do not need to run the following commands, they are here just as a reference:

```
django-admin startproject qogita_api .
python manage.py startapp addresses

python manage.py migrate
python manage.py createsuperuser --email admin@qogita.com --username admin
python manage.py createsuperuser --email admin2@qogita.com --username admin2
```

Two admin users have been created for this project:

Admin:
- email: `admin@qogita.com`
- username: `admin`
- password: `admin`

Admin2:
- email: `admin2@qogita.com`
- username: `admin2`
- password: `admin2`

TODO (filiptanu): Currently the project is using SQLite as a database. Migrate the database setup to a production-ready relational database (e.g. PostgreSQL).

To create a migration for the `Address` model:

```
python manage.py makemigrations addresses
python manage.py migrate addresses
```
