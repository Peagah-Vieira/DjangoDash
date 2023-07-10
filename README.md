# Django Customer Relationship Management

A project for CRM made using Django and Tailwind.

## Functionalities

- Custom login and register authentication
- Password reset with email 
- Dashboard with navbar and sidebar
- Customized tables
- Custom pagination
- Custom search
- Custom empty state
- Flash messages
- Tailwind CSS
- Light and dark theme
- Responsive
- Unit testing, integration testing and functional testing(Selenium)
- Create, read, update, delete(CRUD)

## Screenshots

![LoginAndFlashMessage](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/8bd0c883-6c73-47e7-9609-80aab389b1eb)

![Category](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/db0ce9f6-86a7-430d-96ad-be02917f3f3d)

![DeleteConfirmation](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/ea147f8e-a173-4965-8a37-1e0c9cddb5b1)

![CustomPagination](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/4d914fe2-6b47-49a3-81b8-a74e54734195)

![ThemeSwitch](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/28dc5fec-293a-4ad9-a5bb-235ba825dd78)

## Running locally

Clone the project

```bash
git clone  https://github.com/Peagah-Vieira/Django-CRM
```

Create a virtual environment

```bash
# Linux
sudo apt-get install python3-venv    
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
 .venv\scripts\activate
```

Update the pip

```bash
py -m pip install --upgrade pip
```

Install the dependencies

```bash
pip install -r requirements.txt
npm install
```

Environment variables

```bash
# Django Configuration
SECRET_KEY = 'GENERATE A KEY'

# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'key'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

Compile the Tailwind CSS

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Perform the migrations

```bash
py manage.py migrate
```

Seed leads app

```bash
py manage.py seed leads --number=100
```

Start the server

```bash
py manage.py runserver
```

## Running the tests

To run the tests, run the following command

```bash
coverage run -m pytest 
```

Test percentage table (htmlcov/index.html)

```bash
coverage html
```

## Learnings

Good practice concepts:

(https://learndjango.com/tutorials/django-best-practices-projects-vs-apps).


Python requirements file:

(https://learnpython.com/blog/python-requirements-file/)

Write and run tests:

(https://docs.djangoproject.com/en/4.2/topics/testing/overview/)

Test-Driven Development:

(https://www.browserstack.com/guide/what-is-test-driven-development)

Selenium:

(https://django-selenium.readthedocs.io/en/latest/)

Class Based Views:

(https://docs.djangoproject.com/en/4.2/topics/class-based-views/)

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)





