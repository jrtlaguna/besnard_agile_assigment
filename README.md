# Besnard consulting exam assignment
Simple app with create, update, list, and delete Agile Principles and Values


## Backend configuration
## Local Environment Setup

### Features

- Built using Django and django-restframework

### Requirements
- Python 3.9.2
- Poetry 1.1.5

### Installation
1. Install poetry (https://python-poetry.org/docs/cli/) using `pip install poetry`
2. Initialize poetry using `$poetry shell`
3. Run `$poetry install`

### Initialization

1. Run poetry shell `$poetry shell`
2. Run `$python3 manage.py migrate`
3. Initialize database using `$python manage.py seed`
4. Run `$python manage.py runserver`
### Running unit tests
1. Run `$poetry shell`
2. Run `python manage.py test`


## Frontend Configuration
Features
- Created using Vue 3.0
- Simple CRUD Application

### Requirements
- NodeJS v14.16.1
- VueCLI v6.14.12

### Installation
1. Install Vue cli 
2. run `npm install`

### Getting Started
1. Run `npm run serve`

### Running unit tests
1. Run `$npm run test:unit`