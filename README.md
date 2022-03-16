# API's genereren op basis van het Gemeentelijk Gegevensmodel

Dit is een demonstratieproject om te laten zien hoe je op basis van het [Gemeentelijk Gegevensmodel](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel) API's op basis van [GraphQL](https://graphql.org) kunt genereren. Voor het GraphQl-deel maken we gebruik van [Graphene](https://graphene-python.org). Deze versie bevat een uitwerking van het onderdeel [Onderwijs](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/onderwijs/) gevuld met testdata. In een later stadium voegen we de generatiesoftware toe om ook de andere modellen uit het GGM om te kunnen zetten in werkende API's. 

## Aan de slag

Zorg dat je Docker en [Docker-compose](https://github.com/docker/compose) hebt geïnstalleerd. Dit project maakt gebruik van [Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx). Hier kun je meert informatie vinden over de opbouw van het project.

### Start de container

Om de container te starten doorloop je de volgende stappen (engelstalig)
#### Development

Uses the default Flask development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
    - (M1 chip only) Remove `-slim-buster` from the Python dependency in `services/web/Dockerfile` to suppress an issue with installing psycopg2
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:5000/graphql](http://localhost:5000/graphql). The "web" folder is mounted into the container and your code changes apply automatically.

#### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337/graphql](http://localhost:1337/graphql). No mounted folders. To apply changes, the image must be re-built.

### Test de API's 

Ga naar [http://localhost:1337/graphql](http://localhost:1337/graphql) en je kan queries op de service afvuren. Er zit testdata in voor: leerling, school en inschrijving, hier een voorbeeld van een query. 
![Hier een voorbeeld van een query](/GraphQL.png). 

Veel plezier en succes!