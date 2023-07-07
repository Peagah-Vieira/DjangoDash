# Django Currency Converter

A project made using Django, Currency Converter API, Tailwind.

## Running locally

Clone the project

```bash
git clone  https://github.com/Peagah-Vieira/Django-Curency-Converter
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
SECRET_KEY = 'GENERATE A KEY'
```

Compile the Tailwind CSS

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Perform the migrations

```bash
py manage.py migrate
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

[Currency Converter API](https://rapidapi.com/solutionsbynotnull/api/currency-converter18/)





