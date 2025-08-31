# Travel Booking (Django)
This project is a full-stack web application that allows users to explore available travel options, book tickets, and manage their bookings. It consists of a Django backend for handling authentication, database, and API logic, and a React frontend for an interactive and responsive user interface.

##  Project Structure
/backend    → Django backend (APIs, authentication, database models, booking logic)
/frontend   → React frontend (UI, components, routing, styling)




Backend: Provides REST APIs for user management, travel listings, and bookings.

Frontend: Consumes the backend APIs to display data and provide a seamless user experience.

 ----
 
## Tech Stack

Frontend: React, JavaScript, HTML, CSS, Bootstrap/TailwindCSS

Backend: Django, Django REST Framework (DRF)

Database: SQLite (default, can switch to PostgreSQL/MySQL)

Other Tools: Axios for API calls, Git for version control

-----


## Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Setup Backend (Django)
cd backend

# create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

----

## install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# create superuser (admin panel access)
python manage.py createsuperuser

# start backend server
python manage.py runserver


---

➡ Backend will run at: http://127.0.0.1:8000/

##  Setup Frontend (React)
cd frontend

# install dependencies
npm install

# start frontend server
npm start

----

➡ Frontend will run at: http://localhost:3000/

----

## API Endpoints (Backend)

Some example API routes (Django REST Framework):

POST /api/auth/register/ → Register a new user

POST /api/auth/login/ → Login user

GET /api/travel-options/ → Fetch all travel options

POST /api/bookings/ → Create a booking

GET /api/bookings/ → Get user’s bookings

----


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

Open http://127.0.0.1:8000/register/

## Deploy (Render)
- Build: `pip install -r requirements.txt`
- Start: `gunicorn travel_booking.wsgi`
- Optionally set `DATABASE_URL` for MySQL/Postgres

  -----
  
## Contributing

Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature-xyz)

Commit your changes (git commit -m "Added xyz feature")

Push to the branch (git push origin feature-xyz)

Open a Pull Request

----

## License

This project is licensed under the MIT License – you are free to use, modify, and distribute it.
