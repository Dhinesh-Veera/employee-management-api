# Employee Management API

## Features

- Employee CRUD
- JWT Authentication
- Weather API Integration
- PostgreSQL
- Docker Compose
- Swagger Documentation

## Run

docker compose up --build

## Migrate

docker compose exec web python manage.py migrate

## Create Superuser

docker compose exec web python manage.py createsuperuser