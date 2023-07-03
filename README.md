
# Nome Temporário

Descrição temporária

## Rodando localmente

Clone o projeto

```bash
 git clone  https://github.com/Peagah-Vieira/Django-Dashboard.git
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

Compile o Tailwind CSS

```bash
 npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Realize as migrações

```bash
 py manage.py migrate
```

Inicie o servidor

```bash
 py manage.py runserver
```
## Aprendizados

Conceitos de boas práticas:

(https://learndjango.com/tutorials/django-best-practices-projects-vs-apps).


Arquivo de requisitos do Python:

(https://learnpython.com/blog/python-requirements-file/)


## Documentação

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Tailwind + Flowbite](https://flowbite.com/docs/getting-started/django/)





