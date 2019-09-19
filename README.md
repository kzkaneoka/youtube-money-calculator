# Youtube Money Calculator

It is a web application to calculate the salary of Youtube Channel, built-in Flask & React JS.

## Get Started

Backend code (Flask) is under **backend** directory, and Frontend code (React JS) is under **frontend** directory. You need to install the dependency, set the environment, and run the code individually. Also, it is required to prepare [PostgreSQL](https://www.postgresql.org) and [Youtube Data V3 API key](https://developers.google.com/youtube/v3/).

### Backend (Flask): Install Dependency

```
./backend$ virtualenv -p python3 venv
./backend$ source venv/bin/activate
./backend$ pip install -r requirements.txt
```

### Backend (Flask): Set Environment

```
./backend$ source venv/bin/activate
./backend$ export DATABASE_URL="POSTGRESQL_DATABASE_PATH"
./backend$ python manage.py db init
./backend$ python manage.py db migrate
./backend$ python manage.py db upgrade
./backend$ export DEVELOPER_KEY="YOUTUBE_DATA_V3_API_KEY"
./backend$ export FLASK_ENV= # set FLASK_ENV as one of "dev", "test", or "prod"
```

### Backend (Flask): Run Code

```
./backend$ source venv/bin/activate
./backend$ python manage.py runserver
```

### Backend (Flask): Run Test

```
./backend$ source venv/bin/activate
./backend$ pytest
```

### Frontend (React JS): Install Dependency (React JS Frontend)

```
./frontend$ npm install
```

### Frontend (React JS): Run Code (React JS Frontend)

```
./frontend$ npm start
```

## Task Lists
- [x] Designed a scalable and maintainable file structure, inspired by [Ali Goren](https://dev.to/aligoren/how-i-structure-my-flask-apps-3eh8) and [AJ Pryor](http://alanpryorjr.com/2019-05-20-flask-api-example/).
- [x] Worked on backend and frontend components separately.
- [x] Utilized [a third-party api](https://developers.google.com/youtube/v3/).
- [ ] Tested each component.
- [ ] Secured HTTP request and response transactions.
- [ ] Improved the response time of the backend system using the cache system.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

