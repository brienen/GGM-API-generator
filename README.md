# API's genereren op basis van het Gemeentelijk Gegevensmodel

Dit is een demonstratieproject om te laten zien hoe je op basis van het [Gemeentelijk Gegevensmodel](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel) API's op basis van [GraphQL](https://graphql.org) kunt genereren. Voor het GraphQl-deel maken we gebruik van [Graphene](https://graphene-python.org). Deze versie bevat een uitwerking van het onderdeel [Onderwijs](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/onderwijs/) gevuld met testdata. In een later stadium voegen we de generatiesoftware toe om ook de andere modellen uit het GGM om te kunnen zetten in werkende API's. 

## Aan de slag

Zorg dat je [Docker](https://www.docker.com) en [Docker-compose](https://github.com/docker/compose) hebt geïnstalleerd. Dit project is voortgebouwd op [Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx). Voor het verder tweeken van de container en het koppelen van een andere database vind je hier meer informatie.

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

Ga naar [http://localhost:5000/graphql](http://localhost:5000/graphql) en je kan queries op de service afvuren. Er zit testdata in voor: leerling, school en inschrijving.Hieronder een voorbeeld van een query.

![Hier een voorbeeld van een query](/GraphQL.png).

Veel plezier en succes! Verbeteringen welkom :)

## Enterprise Architect Koppelen

Deze demo werkt met een Enterprise Architect repository in een [Postgres database](https://www.sparxsystems.com/enterprise_architect_user_guide/14.0/model_repository/upsizingtopostgresql.html). Om de repository te openen configureer je een ODBC-koppeling conform de [handleiding van Enterprise Architect](https://www.sparxsystems.com/enterprise_architect_user_guide/14.0/model_repository/setupapostgresqlodbcdriver.html). Het is belangrijk dat je gebruik maakt van een 32-bits-ODBC-driver. Deze demo werkt met Postgres versie 10.20. De benodigde wachtwoorden staan in je .env.dev bestand. 

![Dit zijn de ODBC-instellingen die ik gebruik voor de demo](/ODBC-instellingen.png).

Dit zijn de ODBC-instellingen die ik gebruik voor de demo. Onder OSX gebruik ik een windowsemulator om Enterprise Architect te kunnen draaien. Om de database te kunnen zien gebruik ik het IP-adres 10.211.55.2. Werk je onder Windows dan gebruik je waarschijnlijk localhost (of 127.0.0.1).


![Gebruik Connect Server om te verbinden](/ConnectServer.png).

Nadat je de ODBC-driver hebt geinstalleerd kun je vanuit Enterprise Architect contact maken met de repository. Gebruik hiervoor 'Open Project' --> 'Connect to Server'. Bijgevoegd voorbeeld configuratie-instellingen.

Nadat je de connectie tot stand hebt gebracht kun je gegevensmodellen aanpassen, en op basis hiervan nieuwe API's genereren. 

## API's genereren

Het genereren van API's in deze demo werkt met [Jupyter Notebooks](https://jupyter.org) en Python. Met het notebook [generateCode](http://localhost:8888/lab/tree/generateCode.ipynb) genereer je de API's. De notebooks zijn bereikbaar onder http://localhost:8888.

### Model kiezen

De generator is in staat de API's te genereren van willekeurige modellen uit het GGM. Kies hiervoor de GUID van het package dat je wilt genereren. Voor alle classes die onder dit package vallen (of onder een van de child-packages) wordt een API-specificatie gegenereert. In de volgende afbeelding is getoond hoe je de GUID kiest van het door jou geselecteerde package. In het notebook [generateCode](http://localhost:8888/lab/tree/generateCode.ipynb) zijn als voorbeeld de GUIDs voor 'Monumenten' en 'Onderwijs' meegegeven.

![Selecteer de GUID behorende bij het door jou geselecteerde package](/rootGUID.png).

### Model genereren

Nadat je de GUID van het model hebt gekozen is uitgenereren van de API's makkelijk. Laat hiervoor alle cellen uit het notebook executeren, en de benodigde bestanden worden gegenereerd. 

![Dit kun je in een keer uitvoeren](/restartKernel.png).

Zorg dat je daarna de server herstart door in het console 'docker-compose up' te geven, en zorg dat je het [graphql-scherm](http://localhost:5000/graphql) in je browser te opnieuw laadt. Nu zie je de API's van jouw model in je browser op http://localhost:5000/graphql.

Veel [plezier](https://nl.wiktionary.org/wiki/plezier)! 