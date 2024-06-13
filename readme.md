## Book Review App

It is a django backend that allows users to Create a book and other user s to add review or rate the book.
Features:

- Author with custom model with Token based login and Admin using default django model.
- CRUD operations with book.
- One review/rating per user per book.
- Average ratings per book.
- Search using query parameters.
- Swagger docs

Tech stack:

- Django/DRF
- PostgreSQL

### Backend Setup

- Go to backend folder.
- Create .env in backend folder and create required environment variables including database in postgres. (see `.env.example`)
- Create a new virtual environment: `python -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install packages: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Start server: `python manage.py runserver`
