OSCAR- LATE SHOW API CODE CHALLENGE
The Late Show API is a RESTful API for a late-night TV show application, built with Flask, PostgreSQL, and JWT authentication. It allows users to register, log in, manage episodes, guests, and appearances, with protected routes for creating appearances and deleting episodes.

---

PROJECT STRUCTURE
OSCARLATENIGHTTVSHOW/
├── server/
│ ├── **init**.py
│ ├── app.py
│ ├── config.py
│ ├── db.py
│ ├── seed.py
│ ├── models/
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ ├── appearance.py
│ ├── controllers/
│ │ ├── **init**.py
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ ├── appearance_controller.py
├── migrations/
├── .env
├── .gitignore
├── README.md
├── ShowAPI.postman_collection.json

---

SETUP INSTRUCTIONS
Prerequisites

- Python 3.8+: Ensure Python is installed (python --version).
- PostgreSQL: Install PostgreSQL and ensure it’s running (sudo service postgresql start).
- Postman: Install Postman for testing (Download).
- Pipenv: Install Pipenv for dependency management (pip install pipenv).

---

ENVIRONMENT SETUP

1. Clone the Repository:
   git clone git@github.com:TechTinke/OscarLateNightTvShow.git

2. Set Up PostgreSQL:

- Create a PostgreSQL user and database:psql -U postgres
- CREATE USER maingi WITH PASSWORD 'maingi1122';
- CREATE DATABASE late_showw_db;
- GRANT ALL PRIVILEGES ON DATABASE late_showw_db TO maingi;
- \q

3. Verify connection:psql -U maingi -h localhost -d late_showw_db

- Password: maingi1122
- Exit with \q.

4. Install Dependencies:

- Activate the virtual environment and install packages:pipenv install flask flask-sqlalchemy flask-migrate flask-jwt-extended psycopg2-binary python-dotenv
  pipenv shell

5. Configure Environment Variables:
   Create a .env file in the project root:DATABASE_URL=postgresql://maingi:maingi1122@localhost:5432/late_showw_db
   JWT_SECRET_KEY=9ATallelV47-zLIeRd2_O9ogQ7Z_ZL1fQRB0D46lnWU
   FLASK_RUN_PORT=5008

---

HOW TO RUN

1. Apply Database Migrations:

- export FLASK_APP=server/app.py
- flask db init # Only run once to create migrations folder
- flask db migrate -m "initial migration"
- flask db upgrade

2. Seed the Database:
   Populate the database with sample data:python server/seed.py
   This creates:

- User: admin (password: password)
- Guests: Praise Victoria(Actor), Oscar Maingi(Comedian)
- Episodes: June 1, 2025 (#1), June 2, 2025 (#2)
- Appearances: Ratings 4 and 5 for episode 1

3. Run the Application:

- Start the Flask server on port 5008:flask run --port 5008
- The API will be available at http://localhost:5008.

---

AUTHENTICATION FLOW

- The API uses JWT (JSON Web Token) for authentication. Protected routes (POST /appearances, DELETE /episodes/<id>) require a valid JWT token.

1. Register a User:
   Send a POST request to /register with a username and password.
   Example: {"username": "testuser", "password": "testpassword"}.

2. Log In:
   Send a POST request to /login with the same credentials.
   Response includes an access_token (JWT).
   Example response:{
   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDcxNDQwMywianRpIjoiNTg5YzEyNWUtN2QxZi00YmU2LWI0ZGEtNzBmYTE2YWEzOGZiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNzUwNzE0NDAzLCJjc3JmIjoiOGVjN2EyNzgtMjQ5YS00Zjc3LTg4YmYtYjdiZDUzYWFiNGY0IiwiZXhwIjoxNzUwNzE1MzAzfQ.H90GLmtL_pD0gEsH2K0W1YfN_rMsju7t7cLrZRbe_O0"
   }
   Use the Token:
   Include the token in the Authorization header for protected routes:Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MDcxNDQwMywianRpIjoiNTg5YzEyNWUtN2QxZi00YmU2LWI0ZGEtNzBmYTE2YWEzOGZiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNzUwNzE0NDAzLCJjc3JmIjoiOGVjN2EyNzgtMjQ5YS00Zjc3LTg4YmYtYjdiZDUzYWFiNGY0IiwiZXhwIjoxNzUwNzE1MzAzfQ.H90GLmtL_pD0gEsH2K0W1YfN_rMsju7t7cLrZRbe_O0"

---

ROUTE LIST

1. POST
   /register
   Register a new user
   {"username": "testuser", "password": "testpassword"}
   {"message": "User registered successfully"} (201)

2. POST
   /login
   Log in and get JWT token
   {"username": "testuser", "password": "testpassword"}
   {"access_token": "<jwt-token>"} (200)

3. GET
   /episodes
   List all episodes
   None
   [{"id": 1, "date": "2025-06-01", "number": 1}, ...] (200)

4. GET
   /episodes/<id>
   Get episode details with appearances
   {"episode": {"id": 1, "date": "2025-06-01", "number": 1}, "appearances": [...]} (200)

5. DELETE
   /episodes/<id>
   Delete an episode and its appearances
   {"message": "Episode deleted successfully"} (200)

6. GET
   /guests
   List all guests
   [{"id": 1, "name": "Praise Victoria", "occupation": "Actor"}, ...] (200)

7. POST
   /appearances
   Create a new appearance
   {"rating": 5, "guest_id": 1, "episode_id": 1}
   {"id": 3, "rating": 5, "guest_id": 1, "episode_id": 1} (201)

---

NOTES
Validations:

1. rating in /appearances must be 1–5.
2. guest_id and episode_id must exist.

---

Errors:

- 400: Missing or invalid fields.
- 401: Missing or invalid JWT token.
- 404: Non-existent resource (e.g., episode or guest ID).

---

POSTMAN

1. Import the Collection:

- Open Postman.
- Click File > Import.
- Select ShowAPI.postman_collection.json from the project root.
- Confirm the collection appears as Late Show API Challenge.

2. Create an Environment:

- Go to Environments (sidebar, globe icon) or Manage Environments (gear icon).
- Click Add.
  Name: Late Show API.
  Add a variable:
  Variable: token
  Type: default
  Initial Value: (leave blank)
  Current Value: (leave blank)

3. Save the environment.

- Select Late Show API from the top-right dropdown.

---

UNPROTECTED ROUTES

- Register: Send POST /register with {"username": "testuser", "password": "testpassword"}.
- Login: Send POST /login with the same credentials. Copy the access_token from the response.
- Other Routes: Test GET /episodes, GET /episodes/1, GET /guests.

---

PROTECTED ROUTES

- Ensure the token variable is set.
- Create Appearance: Send POST /appearances with Authorization: Bearer {{token}} and body {"rating": 5, "guest_id": 1, "episode_id": 1}.
- Delete Episode: Send DELETE /episodes/1 with Authorization: Bearer {{token}}.
- Verify responses match the route table.

---

NOTES

The API runs on http://localhost:5008
If errors occur, check server logs (flask run --port 5008) or database connection (psql -U maingi -h localhost -d late_showw_db).
Re-seed the database if needed: python server/seed.py.
