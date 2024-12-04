### INF601 - Advanced Programming in Python
### Samuel Lagle
### Final Project


# Final Project

## Description

This is a web-based application that utilizes the Django framework. The application itself allows for a user to type in a phone number and receive data account data from the popular mobile communication application, WhatsApp.

## Getting Started

```
The commands to initialize the database:
python manage.py makemigrations (this will create any SQL entries that need to go into the database)
python manage.py migrate (this will apply the migrations)

How to create an admin account the utilize the administration functions of the site:
python manage.py createsuperuser
```

### Dependencies

```
The command to install the necessary packages using the provided requirements text file:
pip install -r requirements.txt
```

### Executing program

```
The command to run the development server:
python manage.py runserver
```

## Output

This should run Django to start the server. Next, you can open a browser and type in the URL "http://127.0.0.1:8000" which will allow access to the site. You can register for an account and then login. Afterward, you can use the search functionality to access acount data from the mobile number entered.

## Authors

Samuel Lagle

## Acknowledgments

Inspiration, code snippets, etc.
* [chatgpt](https://chatgpt.com/share/671fe4e6-45ec-8010-ba09-c72008ca1266)
* [Django](https://docs.djangoproject.com/en/4.2/intro/)
* [Bootstrap](https://getbootstrap.com/docs/5.3/components/modal/)
