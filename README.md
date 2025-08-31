# Travel Booking (Django)

## Run locally
```bash
python -m venv venv_travel
venv_travel\Scripts\activate   # Windows
# source venv_travel/bin/activate  # macOS/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Deploy (Render)
- Build: `pip install -r requirements.txt`
- Start: `gunicorn travel_booking.wsgi`
- Optionally set `DATABASE_URL` for MySQL/Postgres
