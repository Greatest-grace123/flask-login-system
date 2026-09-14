# Flask Login System 🔐

A beginner-friendly user authentication system built with Flask, SQLite, and SQLAlchemy.

## Features

* User registration
* User login and logout
* Password hashing
* Password confirmation
* Password length validation
* Duplicate username detection
* Session-based authentication
* Protected dashboard
* Flash messages
* Show/hide password
* Environment variables for secret keys
* Git and GitHub version control

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Werkzeug
* HTML
* CSS
* JavaScript
* Git
* GitHub

## Project Structure

```text
flask_login_system/
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── static/
    └── style.css
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Greatest-grace123/flask-login-system.git
```

### 2. Enter the project folder

```bash
cd flask-login-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Git Bash:

```bash
source .venv/Scripts/activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

### 6. Create your `.env` file

Create a `.env` file in the project folder and add:

```text
SECRET_KEY=your-secret-key
```

### 7. Start the Flask application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## What I Learned

This project helped me understand how authentication works in a web application, including user registration, password hashing, login sessions, protected routes, validation, and basic project security.

It also gave me practical experience using Git and GitHub to manage and publish a software project.
