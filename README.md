Late Show API Challenge
A Flask REST API for managing a Late Night TV show system with PostgreSQL, JWT authentication, and MVC architecture.
Setup Instructions
Prerequisites

Python 3.9+
PostgreSQL
Git
Postman

Installation

Clone the repository:
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge

Set up a virtual environment with Pipenv:
pip install pipenv
pipenv install
pipenv shell

Install PostgreSQL and create a database:
psql -U postgres
CREATE DATABASE late_show_db;
\q

Create a .env file in the root directory:
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/late_show_db
JWT_SECRET_KEY=your-very-secure-secret-key

Set up the database:
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py

Run the application:
python server/app.py

Authentication Flow

Register: Create a user account via POST /register with a JSON body:
{
"username": "admin",
"password": "password"
}

Response:
{
"message": "User registered successfully"
}

Login: Obtain a JWT token via POST /login with the same JSON body:Response:
{
"access_token": "<your-jwt-token>"
}

Protected Routes: Include the token in the Authorization header:
Authorization: Bearer <your-jwt-token>

API Routes

Route
Method
Auth Required?
Description

/register
POST
No
Register a new user

/login
POST
No
Log in and get JWT token

/episodes
GET
No
List all episodes

/episodes/<id>
GET
No
Get episode details and appearances

/episodes/<id>
DELETE
Yes
Delete episode and its appearances

/guests
GET
No
List all guests

/appearances
POST
Yes
Create a new appearance

Sample Request/Response
GET /episodes/1Response:
{
"episode": {
"id": 1,
"date": "2025-06-01",
"number": 1
},
"appearances": [
{
"id": 1,
"rating": 4,
"guest_id": 1,
"episode_id": 1
}
]
}

POST /appearancesRequest:
{
"rating": 5,
"guest_id": 1,
"episode_id": 1
}

Response:
{
"id": 3,
"rating": 5,
"guest_id": 1,
"episode_id": 1
}

Postman Testing

Import the challenge-4-lateshow.postman_collection.json into Postman.
Register a user and log in to obtain a JWT token.
Set the token in the Authorization header for protected routes (Bearer Token).
Test all routes to ensure they return expected responses.

GitHub Repository
https://github.com//late-show-api-challenge
