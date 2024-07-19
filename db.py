from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'booking_db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Booking(db.Model):
    __tablename__ = 'list_table'
    booking_id = db.Column(db.Integer, primary_key=True)
    select_room = db.Column(db.String(40), nullable=False)
    email_address = db.Column(db.String(40), nullable=False)
    check_in = db.Column(db.String(40), nullable=False)
    check_out= db.Column(db.String(40), nullable=False)


def __init__(self, select_room, email_address, check_in, check_out):
    self.select_room = select_room
    self.email_address = email_address
    self.check_in = check_in
    self.check_out = check_out

class Login(db.Model):
    __tablename__ = 'login_table'
    login_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)

def __init__(self, email_address, password):
    self.email_address = email_address
    self.password = password

class Register(db.Model):
    __tablename__ = 'register_table'
    register_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email_address = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)
    password= db.Column(db.String(40), nullable=False)
    confirm_password = db.Column(db.String(40), nullable=False)

def __init__(self, first_name, last_name, email_address, phone_number, password, confirm_password):
    self.first_name = first_name
    self.last_name = last_name
    self.email_address = email_address
    self.phone_number = phone_number
    self.password = password
    self.confirm_password = confirm_password

@app.route('/')
def index():
    return render_template('bookings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/activitiesPage')
def activitiesPage():
    return render_template('activitiesPage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/accommodation')
def accommodation():
    return render_template('accommodation.html')

@app.route('/mars')
def mars():
    return render_template('mars.html')

@app.route('/venus')
def venus():
    return render_template('venus.html')

@app.route('/jupiter')
def jupiter():
    return render_template('jupiter.html')

@app.route('/saturn')
def saturn():
    return render_template('saturn.html')

@app.route('/activityBook')
def activityBook():
    print("in activity book")
    return render_template('activityBook.html')

@app.route('/bookings')
def bookings():
    return render_template('bookings.html')

@app.route('/bookings', methods=['POST'])
def submit_booking():
    try:
        select_room = request.form['select_room']
        email_address = request.form['email_address']
        check_in = request.form['check_in']
        check_out = request.form['check_out']

        new_booking = Booking(
            select_room=select_room,
            email_address=email_address,
            check_in=check_in,
            check_out=check_out
        )

        db.session.add(new_booking)
        db.session.commit()
        print('Details entered successfully!')
    except Exception as e:
        # If an error occurs, roll back the transaction
        db.session.rollback()
        print(e)
        print('An error occurred while booking the class.')
    return f"Booking received for {email_address} to {select_room} from {check_in} to {check_out}."

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/login', methods=['POST'])
def submit_login():
    try:
        email_address = request.form['email_address']
        password = request.form['password']

        new_login = Login(
            email_address=email_address,
            password=password
        )

        db.session.add(new_login)
        db.session.commit()
        print('Login Successful!')
    except Exception as e:
        # If an error occurs, roll back the transaction
        db.session.rollback()
        print(e)
        print('An error occurred while logging in.')
    return f"Login received for {email_address}."

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def submit_register():
    try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email_address']
        phone_number = request.form['phone_number']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        new_register = Register(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            password=password,
            confirm_password=confirm_password
        )

        db.session.add(new_register)
        db.session.commit()
        print('Registration Successful!')
    except Exception as e:
        # If an error occurs, roll back the transaction
        db.session.rollback()
        print(e)
        print('An error occurred while registering.')
    return f"Registration received for {first_name} {last_name} at {email_address}."

if __name__ == '__main__':
    app.run(debug=True)