# Qogita interview assignment

This repository contains implementation of the specification defined in [back-end-engineer-assessment.md](back-end-engineer-assessment.md).

## Requirements

- Docker
- Docker Compose

## Running the API

To run the API, run:

```
docker-compose run --service-ports api
```

To run the integration tests, run:

```
docker-compose run postman
```
## Development references

```
django-admin startproject qogita_api .
python manage.py startapp addresses

python manage.py migrate
python manage.py createsuperuser --email admin@qogita.com --username admin
python manage.py createsuperuser --email admin2@qogita.com --username admin2

python manage.py makemigrations addresses
python manage.py migrate addresses
```
