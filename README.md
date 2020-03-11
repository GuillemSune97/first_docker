<h1>Docker Study</h1>

<h2>Summary</h2>
<p>I wanted to learn Docker, so I'm making this project to follow Docker's documentation & work teammates to learn how it works.</p>
<p>At the same time, I'm doing the <a href="https://tutorial.djangogirls.org/en/">Django Girls tutorial</a> to learn Python and Django.</p>
<p><i>I'm only going to explain the Docker part.</i></p>

<h2>Docker</h2>
<p>Lorem ipsum</p>

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

django girls checkpoint: <a href="https://tutorial.djangogirls.org/en/extend_your_application/">aquí</a>