# Qogita interview assignment

This repository contains implementation of the specification defined in [back-end-engineer-assessment.md](back-end-engineer-assessment.md).

## Requirements

- Python 3

In order to isolate this project's dependencies from the rest of the system, you can create and use a virtual environment:

```
python3 -m venv qogita-api-venv
source qogita-api-venv/bin/activate
```

To install the project's dependencies:

```
python -m pip install -r requirements.txt
```

To run the project:

```
cd qogita_api
python manage.py runserver
```

## Reference

TODO (filiptanu): Maybe remove this section in the future

This project has been generated using `django-admin`. You do not need to run the following commands, they are here just as a reference:

```
django-admin startproject qogita_api
cd qogita_api
python manage.py startapp addresses

python manage.py migrate
python manage.py createsuperuser --email admin@qogita.com --username admin
```

An admin user has been created for this project:

- email: `admin@qogita.com`
- username: `admin`
- password: `admin`

TODO (filiptanu): Currently the project is using SQLite as a database. Migrate the database setup to a production-ready relational database (e.g. PostgreSQL).

To create a migration for the `Address` model:

```
python manage.py makemigrations addresses
python manage.py migrate addresses
```
