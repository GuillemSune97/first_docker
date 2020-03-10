<h2>Steps to get the django running:</h2>

Create the containers from their images:
```bash
$ docker-compose build
```

We run the containers and go into django's bash:
```bash
$ docker-compose run --rm --service-ports django bash
```

Migrate the django database to the db service on the db container (?):
```bash
$ python manage.py migrate
```

Continue