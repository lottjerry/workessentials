from flask import render_template, redirect, url_for
import flask_login
from flask_login import login_manager
from flask_login.login_manager import LoginManager
from werkzeug.utils import redirect
from workessentials import app, db
from workessentials.forms import LoginForm, RegisterForm
from workessentials.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Check if the user exists in the database
        user = User.query.filter_by(username=form.username.data).first()
        # If the user exists then check to see if the password match
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1> Invalid username or password </h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        # Creates a new user giving the information from the sign up form
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Add that user to the database and commit changes
        db.session.add(new_user)
        db.session.commit()
        
        return '<h1> New user has been created! </h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))