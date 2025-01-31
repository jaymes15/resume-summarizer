# Resume Summarizer

Written with [Django](https://www.djangoproject.com/) and [DRF](https://www.django-rest-framework.org/)

## Requirements to run this project using Docker

- docker (20.10.5+): To install docker visit https://docs.docker.com/get-docker/
- docker-compose (1.25.5+): To install docker-compose visit https://docs.docker.com/compose/install/


## Getting started

**To start project with Docker:**
 - install docker
 - install docker-compose
 - Clone the project  
 - Change directory to the project directory 
 - Run `cp .sample.build.env .env`
 - Run:
    ```bash
        docker-compose up
    ```
  - The application would be available at http://127.0.0.1:8000

## API Docs
You can find the API docs at http://localhost:8000/api_docs/
## Project commands using docker

Start a new app:

```bash
docker-compose run --rm app sh -c "python manage.py startapp {app_name}"
```

Create superuser:

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Makemigrations:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py makemigrations"
```

To migrate:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
```

To makemigrations and migrate:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && && python manage.py makemigrations && python manage.py migrate"
```

To run test suites:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"
```

To check lint:

```bash
docker-compose run --rm app sh -c "flake8"
```

To run tests and check lint:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"
```

To install new packages:

Add the package name to  ```requirement.txt``` file
then run 

```bash
docker-compose up --build
```

To tear down the all containers:

```bash
docker-compose down
```

isort:

```bash
docker-compose run --rm app sh -c "isort ."
```
