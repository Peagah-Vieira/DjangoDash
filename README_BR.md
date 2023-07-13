[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Peagah-Vieira/Django-CRM/blob/main/README_BR.md)
# Django Customer Relationship Management

Um projeto para CRM feito usando Django e Tailwind.

## Funcionalidades

- Login personalizado e autenticação de registro

- Redefinição de senha com e-mail

- Painel com barra de navegação e barra lateral

- Tabelas personalizadas

- Paginação personalizada

- Pesquisa personalizada

- Estado vazio personalizado

- Django-Admin personalizado

- Exportação Excel

- mensagens instantâneas

- CSS Tailwind

- Tema claro e escuro

- Responsivo

- Teste de unidade, teste de integração e teste funcional (Selenium)

- Criar, ler, atualizar, excluir (CRUD)

## Capturas de tela

<details>
  <summary>Cadastro e Login</summary>

  ![Register_Login](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d81ff8de-c579-4546-889b-d5b63afec74d)

</details>

<details>
  <summary>Criar</summary>

  ![Create](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/6b9a2a65-4046-4dde-9734-079c536675b1)

</details>

<details>
  <summary>Atualizar</summary>

  ![Update](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/03135f00-a153-45de-8f2d-40541bd2372b)

</details>

<details>
  <summary>Deletar</summary>

  ![Delete](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/5406f43a-888c-4a9a-90ca-bd53eda2c632)

</details>

<details>
  <summary>Paginação customizada</summary>

  ![Pagination](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/a832c505-0748-409d-8d41-ad810542d55f)

</details>

<details>
  <summary>Tema claro e escuro</summary>

  ![Theme_Switch](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/263b1a74-1293-4249-a97a-6b3a106ac56d)

</details>

<details>
  <summary>Pesquisa e estado vazio</summary>

  ![Search_Empty_State](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/63e186ff-de33-4597-8eac-6bb500ba506a)

</details>

<details>
  <summary>Exportação para o excel</summary>

  ![Export](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/d3a645d4-493a-4981-a5b3-db82667f9a68)

</details>

<details>
  <summary>Responsivo</summary>

  ![Responsive](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/3ea69c94-75a5-4f8e-a916-3487b101a0e1)

</details>

<details>
  <summary>Django admin customizado</summary>

  ![Django-Admin](https://github.com/Peagah-Vieira/Django-CRM/assets/105545343/944a29ab-8c9e-4f3e-b31b-b259cc772046)

</details>

## Executando localmente

Clone o projeto

```bash
git clone  https://github.com/Peagah-Vieira/Django-CRM
```

Crie um ambiente virtual

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

Atualize o pip

```bash
py -m pip install --upgrade pip
```

Instale as dependências

```bash
pip install -r requirements.txt
npm install
```

Alterar variáveis ​​de ambiente

```bash
# Django Configuration
# SECRET_KEY = 'GENERATE A KEY'

# SMTP Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'CHANGE-ME'
# EMAIL_HOST_PASSWORD = 'CHANGE-ME'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

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

Configure settings.py

```bash
# Local Configuration
DATABASES = {
  'default': {
      'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
      'NAME': os.getenv('POSTGRES_DB', BASE_DIR / './db.sqlite3'),
      'USER': os.getenv('POSTGRES_USER', ''),
      'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
      'HOST': os.getenv('POSTGRES_HOST', ''),
      'PORT': os.getenv('POSTGRES_PORT', ''),
  }
}

# Deploy - Render Configuration
# DATABASE_URL = os.getenv('DATABASE_URL')
# DATABASES = {
#    'default': dj_database_url.config(),
# }
```

Compilar o Tailwind CSS

```bash
npm run build 
```

Realize as migrações

```bash
py manage.py migrate
```

Semear aplicativo leads

```bash
py manage.py seed leads --number=50
```

Iniciar o servidor

```bash
py manage.py runserver
```

## Executando os testes

Para executar os testes, execute o seguinte comando

```bash
coverage run -m pytest 
```

Tabela de porcentagem de teste (htmlcov/index.html)

```bash
coverage html
```

## Aprendizados

Conceitos de boas práticas:

(https://learndjango.com/tutorials/django-best-practices-projects-vs-apps).

Arquivo de requisitos do Python:

(https://learnpython.com/blog/python-requirements-file/)

Escreva e execute testes:

(https://docs.djangoproject.com/en/4.2/topics/testing/overview/)

Desenvolvimento Orientado a Testes:

(https://www.browserstack.com/guide/what-is-test-driven-development)

Selenium:

(https://django-selenium.readthedocs.io/en/latest/)

Exibições baseadas em classe:

(https://docs.djangoproject.com/en/4.2/topics/class-based-views/)

PostgreSQL - Convenções de nomenclatura:

(https://www.geeksforgeeks.org/postgresql-naming-conventions/)

## Documentação

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)

[Django Custom Taiwind](https://github.com/Aleksi44/django-admin-tailwind)
