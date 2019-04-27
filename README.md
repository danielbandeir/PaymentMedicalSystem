# Paymment medical system

Hi, my name is Daniel :wave: and I developed this open-source payment system that create multiples datasheet, to person and historic payment

## Understand the structure folder

In this structure you have the central and the requirements, in central you have all the modules, database model, templates, you have all the projects rs, and requirements is where you go found the rigth libs to run the project.

## The requirements

In the requirements we have this packages:

```
dj-database-url==0.5.0
Django==2.1.7
django-heroku==0.3.1
gunicorn==19.9.0
psycopg2==2.7.7
pytz==2018.9
whitenoise==4.1.2
```

This project is configured to just deploy in Heroku using the Django =D

## Installing

First of all you have to do this commands to create the local virtual environment:

```
pip install virtualenvironment
```

**WARNING: IN THIS STEP FOR USE PIP YOU NEED THE PYTHON INSTALLED IN YOUR LOCAL MACHINE**

After crate the virtual environment and names him, you run this command to install requirements with virtual environment actived:

```
pip install -r requirements.txt
```

## Running

For acess the system in your local machine you have to run runserver, in your structure folder run:

```
python manage.py runserver
```

Now you can acess the system in localhost:8000, or 127.0.0.1:8000/

## Login

By default the login and password for system is:

```
login: admin
password: admin
```

If you want to create a new user for acess the /admin page, you have to run this command to create your own login

```
python manage.py createsuperuser
```

### Let's go to work! =D

