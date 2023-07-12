# Django Customer Relationship Management

A project for CRM made using Django and Tailwind.

## Functionalities

- Custom login and register authentication
- Password reset with email 
- Dashboard with navbar and sidebar
- Custom tables
- Custom pagination
- Custom search
- Custom empty state
- Custom Django-Admin
- Excel export
- Flash messages
- Tailwind CSS
- Light and dark theme
- Responsive
- Unit testing, integration testing and functional testing(Selenium)
- Create, read, update, delete(CRUD)

## Screenshots

<details>
  <summary>Register and login</summary>
  
  ![Register_Login](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d81ff8de-c579-4546-889b-d5b63afec74d)
  
</details>

<details>
  <summary>Create</summary>
 
  ![Create](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/6b9a2a65-4046-4dde-9734-079c536675b1)
  
</details>

<details>
  <summary>Update</summary>
 
  ![Update](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/03135f00-a153-45de-8f2d-40541bd2372b)
  
</details>

<details>
  <summary>Delete confirmation</summary>
 
  ![Delete](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/5406f43a-888c-4a9a-90ca-bd53eda2c632)
  
</details>

<details>
  <summary>Custom pagination</summary>

  ![Pagination](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/a832c505-0748-409d-8d41-ad810542d55f)
  
</details>

<details>
  <summary>Dark and light theme</summary>
 
  ![Theme_Switch](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/263b1a74-1293-4249-a97a-6b3a106ac56d)
  
</details>

<details>
  <summary>Search and empty state</summary>
 
  ![Search_Empty_State](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/63e186ff-de33-4597-8eac-6bb500ba506a)
  
</details>

<details>
  <summary>Excel Export</summary>
 
  ![Export](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d3a645d4-493a-4981-a5b3-db82667f9a68)
  
</details>

<details>
  <summary>Responsive</summary>
 
  ![Responsive](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/3ea69c94-75a5-4f8e-a916-3487b101a0e1)
  
</details>

<details>
  <summary>Django Custom Admin</summary>
 
  ![Django-Admin](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/944a29ab-8c9e-4f3e-b31b-b259cc772046)
  
</details>

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
# Django Configuration
SECRET_KEY = 'GENERATE A KEY'

# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'CHANGE-ME'
EMAIL_HOST_PASSWORD = 'CHANGE-ME'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Sqlite Configuration
# DATABASE_ENGINE = 'django.db.backends.sqlite3'
# DATABASE_NAME = './db.sqlite3'


# PostgreSQL Configuration
# DATABASE_ENGINE = 'django.db.backends.postgresql'
# DATABASE_NAME = "CHANGE-ME"
# DATABASE_USER = "CHANGE-ME"
# DATABASE_PASSWORD = "CHANGE-ME"
# DATABASE_HOST = "127.0.0.1"
# DATABASE_PORT = "5432"

# PostgreSQL Docker Configuration
# DB_ENGINE = "django.db.backends.postgresql"
# POSTGRES_DB = "CHANGE-ME"
# POSTGRES_USER = "CHANGE-ME"
# POSTGRES_PASSWORD = "CHANGE-ME"
# POSTGRES_HOST = "localhost"
# POSTGRES_PORT = "5432"
```

Compile the Tailwind CSS

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css 
```

Perform the migrations

```bash
py manage.py migrate
```

Seed leads app

```bash
py manage.py seed leads --number=50
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

PostgreSQL - Naming Conventions:

(https://www.geeksforgeeks.org/postgresql-naming-conventions/)

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)

[Django Custom Taiwind](https://github.com/Aleksi44/django-admin-tailwind)





