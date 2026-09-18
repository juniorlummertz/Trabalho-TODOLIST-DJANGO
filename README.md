# Django Task List

A server-rendered task management application built with Django. Users can create, complete, and delete tasks through a responsive interface protected by CSRF tokens.

## Features

- Create tasks
- Mark tasks as completed
- Delete tasks
- Pending-first ordering
- Server-side rendering with Django templates
- CSRF-protected form actions
- Automated view tests
- Responsive interface

## Tech stack

- Python 3
- Django 6
- SQLite
- HTML5 and CSS3

## Run locally

```bash
git clone https://github.com/juniorlummertz/Trabalho-TODOLIST-DJANGO.git
cd Trabalho-TODOLIST-DJANGO
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Then install and start the application:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Tests

```bash
python manage.py test
```

## Author

Marcio Junior Lummertz — Systems Analysis and Development student.
