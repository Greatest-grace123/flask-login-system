from flask import Flask, render_template, request, session, redirect, url_for, flash
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect SQLAlchemy to Flask
db = SQLAlchemy(app)


# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Create the database
with app.app_context():
    db.create_all()


# Home page
@app.route("/")
def home():
    return "My Login System is Working!"


# Registration page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check if username is empty
        if not username:
            flash("Username cannot be empty!")
            return redirect(url_for("register"))

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        # Check password length
        if len(password) < 6:
            flash("Password must be at least 6 characters!")
            return redirect(url_for("register"))

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = User(
            username=username,
            password=hashed_password
        )

        # Save user to database
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!")
        return redirect(url_for("login"))

    return render_template("register.html")


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Find the user in the database
        user = User.query.filter_by(username=username).first()

        # Check username and password
        if user and check_password_hash(user.password, password):

            # Remember the logged-in user
            session["user_id"] = user.id

            # Go to dashboard
            return redirect(url_for("dashboard"))

        # Wrong username or password
        flash("Invalid username or password!")
        return redirect(url_for("login"))

    # Show login page
    return render_template("login.html")



# Dashboard
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    if user is None:
        session.pop("user_id", None)
        flash("User account not found.")
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=user.username)


# Logout


# Logout
@app.route("/logout")
def logout():

    session.pop("user_id", None)

    flash("You have been logged out.")

    return redirect(url_for("login"))


# Start the application
if __name__ == "__main__":
    app.run(debug=True)