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
- Create security key
- Or paste this instead SECRET_KEY=django-insecure-zf@gpw2t&ri#uw7@d8^#&#nkdpawfouz9dj^p*ii$mz-412jpm

## Run migrations:
- python manage.py makemigrations
- python manage.py migrate

### Generate dummy data for your database
- python manage.py generate_data.py

## Create admin user
- python manage.py createsuperuser 
- details: user=admin, pass=2020flex

## Start development server
- python manage.py runserver 13000

## API Guide.
- Find API guides in docs folder inside project.