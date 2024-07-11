from flask import Flask, request, flash, url_for, redirect, session, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Enum, case
from datetime import datetime
import re

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'voyager'

app = Flask(__name__, template_folder='website/templates', static_folder='website/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'root'
db = SQLAlchemy(app)


class RegistrationForm(db.Model):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(db.Model):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class BookingForm(db.Model):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    check_in = DateField('Check-in Date', validators=[DataRequired()])
    check_out = DateField('Check-out Date', validators=[DataRequired()])
    room_type = SelectField('Room Type', choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')],
                            validators=[DataRequired()])
    submit = SubmitField('Book')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(emai=form.email.date).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = BookingForm()
    if form.validate_on_submit():
        new_booking = Booking(
            name=form.name.data,
            email=form.email.data,
            check_in=form.check_in.data,
            check_out=form.check_out.data,
            room_type=form.room_type.data,
            user_id=current_user.id
        )
        db.session.add(new_booking)
        db.session.commit()
        flash('Your booking has been made', 'success')
        return redirect(url_for('index'))
    return render_template('booking.html', form=form)


@app.route('/manage_bookings')
@login_required
def manage_bookings():
    bookings = Booking.query.filter_by(user_id=currrent_user.id).all()
    return render_template('manage_bookings.html', bookings=bookings)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if _name_ == '_main_':
    app.run(debug=True)

# Database configuration
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'voyager'

# Initialize the Flask application and specify the template and static folders
app = Flask(__name__, template_folder='website/template', static_folder='website/static')

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
