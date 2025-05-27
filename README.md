# Estudo do framework django
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/alexsanderkafka/study-django-api/blob/main/LICENSE) 

# Sobre o projeto
Criado uma api rest com objetivo de realizar um CRUD

## UML
![der]

# Tecnologias utilizadas
## Back end
- Python
- django framework

## Banco de dados
- MySQL

# Como executar o projeto

## Back end
Pré-requisitos: Python instalado, esse projeto foi feito na versão 3.13.3

```bash
# clonar repositório
git clone https://github.com/alexsanderkafka/study-django-api.git

# criar o banco de dados

# configurar o .env
DB_NAME=set name
DB_USER=set user
DB_PASSWORD=set password
DB_HOST=set host
DB_PORT=set port

# criar e configurar o ambiente virtual
python -m venv venv
cd ./venv/Scripts
.\activate

# instalação de dependências no ambiente virtual
pip install django djangorestframework
pip install python-decouple
pip install mysqlclient

# migrations
python manage.py makemigrations
python manage.py migrate

# executar o projeto
python manage.py runserver
```
