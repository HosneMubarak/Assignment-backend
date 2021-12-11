## Flight Assignment Frontend

In the project directory, you can run:

*Please Make sure backend project server is running 8000 port and frontend 3000 port*
### `pip install -r requirements.txt`
### `python manage.py makemigration`
### `python manage.py migrate`
### `python manage.py runserver 8000`

##For Running Docker:

### `docker-compose up -d --build`
### `docker-compose exec web python manage.py makemigrations`
### `docker-compose exec web python manage.py migrate`

