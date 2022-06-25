## Quick Guide

### Clone project: 
- git clone https://github.com/siphesihlemagazi/Bank-API.git
- Or download it directly from https://github.com/siphesihlemagazi/Bank-API

### Create virtual environment
- python -m venv bank-api-venv

### Activate virtual environment
- Windows: bank-api-venv\Scripts\activate 
- Linux:  source bank-api-venv/bin/activate

### Install the requirements found in project dir
- pip install -r requirements.txt

### Create app security key
- Create .env file inside /bank_api
- Run this code to generate key:
`from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())`[_code snippet_ source](https://www.educative.io/answers/how-to-generate-a-django-secretkey)
- Paste your secret key in your .env file:
`SECRET_KEY=your-secrete-key`

## Run migrations:
- python manage.py makemigrations
- python manage.py migrate

### Generate dummy data for your database
- python manage.py generate_data.py

## Create admin user
- python manage.py createsuperuser 
- details: user=admin, password=password

## Start development server
- python manage.py runserver 13000

## API Guide.
- Find API guides in docs folder inside project.