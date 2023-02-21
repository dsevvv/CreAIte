import os

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            token = secrets.token_urlsafe(32)
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'), token=token, confirmed_email=False)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            generate_confirmation_email(new_user)
            flash('Account created! Please check your email to confirm your account.', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/confirmation/<token>')
def confirmation(token):
    # Verify that the token is valid (i.e., it exists in the database)
    if is_confirmation_token_valid(token):
        # Get the user's email associated with the token
        user = User.query.filter_by(token=token).first()
        user.confirmed_email = True
        db.session.commit()

        # Redirect the user to a page that confirms their email address
        flash('Account confirmed! You now have access to all CreAIte features!', category='success')
        return redirect(url_for('views.home'))

    # If the token is not valid, display an error message
    flash('Invalid confirmation link')
    return redirect(url_for('login'))


def generate_confirmation_email(user):
    token = user.token
    confirm_url = url_for('auth.confirmation', token=token, _external=True)
    send_email(user.email, confirm_url)


def send_email(recipient, confirm_url):
    sender = os.getenv('MAIL_USER')
    subject = 'CreAIte Account Confirmation'
    body = f'''Thank you for signing up for CreAIte! \n\nPlease click the following link to confirm your email address: {confirm_url}'''

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    smtp_server = 'smtp.gmail.com'
    port = 587
    smtp_user = os.getenv('MAIL_USER')
    smtp_pass = os.getenv('MAIL_PASS')

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(sender, recipient, msg.as_string())


def is_confirmation_token_valid(token):
    # Check if the token is valid
    if User.query.filter_by(token=token).first():
        return True
    else:
        return False
