# djangoNews

## Description
This is the source code of the test task in Django.

## Technologies
* Python (3.7.3)
* PostgreSQL (11.4)
* Django (3.1)

## Install
In the project directory root run following command. You will need to have docker-compose installed on your machine.
```
docker-compose up -d --build
```
Apply migrations:
```
docker-compose exec web python manage.py migrate --noinput
```
## Postman collection link
https://www.getpostman.com/collections/4622922f1f9fdd90d4d0

## Deployment link
https://django-test-task.herokuapp.com/
