**1) Issue Tracker API:**

A RESTful Issue Tracker API built with Python and FastAPI. This project provides a backend service for creating, viewing, updating, and deleting software issues through API endpoints.

**2) Features:**

Create a new issue

Retrieve all issues

Retrieve a specific issue by ID

Update issue information

Delete an issue

Request and response validation

RESTful API design

Interactive API documentation with Swagger UI

FastAPI automatic documentation

**3) Technologies Used:**

Python

FastAPI

Pydantic

Uvicorn

**5) Installation:**

**Clone the repository:**
git clone https://github.com/ih8asham/issue-tracker-api.git

**Go to the project directory:**
cd issue-tracker-api

**Create a virtual environment:**
python -m venv venv

**Activate the virtual environment on Windows:**
venv\Scripts\activate

**Install the required packages:**
pip install -r requirements.txt

**6) Run the API:**

**Start the FastAPI development server:**
uvicorn main:app --reload

**The API will be available at:**
http://127.0.0.1:8000

**7) API Documentation**

**After starting the server, open:**
http://127.0.0.1:8000/docs

Swagger UI allows you to view and test the available API endpoints directly from your browser.

**Alternative documentation:**
http://127.0.0.1:8000/redoc

**8) API Endpoint**

The Issue Tracker API uses an issue-related route for managing issues.

**Example:**
/api/v1/issues

**Typical operations include:**

GET     /api/v1/issues

GET     /api/v1/issues/{issue_id}

POST    /api/v1/issues

PUT     /api/v1/issues/{issue_id}

DELETE  /api/v1/issues/{issue_id}

The exact available methods and paths depend on the current project implementation.

**9) Security**

Do not upload passwords, API keys, database credentials, .env files, or other sensitive information to GitHub.

The virtual environment folder should also not be uploaded.

**Author:**
Muhammad Ihtasham

GitHub: https://github.com/YOUR_USERNAME
