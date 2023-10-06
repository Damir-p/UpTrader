# MENU 

## COPY:
```sh
$ git clone https://github.com/Damir-p/UpTrader.git
```

## VIRTUALENV
```sh
$ python3 -m venv venv
```

## ACTIVATE VENV
```sh
$ source venv/bin/activate
```

## INSTALL REQUIREMENTS
```sh
(venv)$ pip install -r requirements.txt
```

## MIGRATIONS
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```

## CREATESUPERUSER
```sh
(venv)$ python manage.py createsuperuser
name: "admin"
email: ""
password: "password"
enter: "y"
```

## RUN
```sh
(venv)$ python manage.py runserver 127.0.0.1:8000
```

## CREATE MENU
```sh
(venv)$ 127.0.0.1:8000/admin/
```
