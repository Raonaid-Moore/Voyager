from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'activity.db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Activity(db.Model):
    __tablename__ = 'activity_bookings'
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(40), nullable=False)
    customer_name = db.Column(db.String(40), nullable=False)
    activity_date = db.Column(db.String(40), nullable=False)
    customer_email = db.Column(db.String(40), nullable=False)
    customer_phone = db.Column(db.String(40), nullable=False)
    activity_time = db.Column(db.String(40), nullable=False)


def __init__(self, activity_name, customer_name, activity_date, customer_email, customer_phone, activity_time):
    self.activity_name = activity_name
    self.customer_name = customer_name
    self.activity_date = activity_date
    self.customer_email = customer_email
    self.customer_phone = customer_phone
    self.activity_time = activity_time

@app.route('/')
def index():
    print("in index")
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/activitiesPage')
def activitiesPage():
    print("in get activities page")
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

@app.route('/funfacts')
def funfacts():
    print("in funfacts")
    return render_template('funfacts.html')

@app.route('/astronaut')
def astronaut():
    print("in astronaut")
    return render_template('astronaut.html')

@app.route('/JungleGym')
def JungleGym():
    print("in Jungle Gym")
    return render_template('JungleGym.html')

@app.route('/LowGravityTrampoline')
def LowGravityTrampoline():
    print("in Low Gravity Trampoline")
    return render_template('LowGravityTrampoline.html')

@app.route('/ZeroGravityBallPit')
def ZeroGravityBallPit():
    print("in Zero Gravity Ball Pit")
    return render_template('ZeroGravityBallPit.html')

@app.route('/spacesuit')
def spacesuit():
    print("in spacesuit")
    return render_template('spacesuit.html')

@app.route('/transportbookings')
def transportbookings():
    print("in transport bookings")
    return render_template('transportbookings.html')

@app.route('/restaurant')
def restaurant():
    print("in restaurant")
    return render_template('restaurant.html')

@app.route('/offers')
def offers():
    print("in offers")
    return render_template('offers.html')

@app.route('/privacy')
def privacy():
    print("in privacy")
    return render_template('privacy.html')

@app.route('/bookings')
def bookings():
    print("in bookings")
    return render_template('bookings.html')

@app.route('/payment')
def payment():
    print("in payment")
    return render_template('payment.html')

@app.route('/payment')
def payment():
    print("in payment")
    return render_template('payment.html')

@app.route('/booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    activity = request.form['activity']
    date = request.form['date']
    time = request.form['time']
    new_activity = Activity(activity_name=activity, customer_name=name, activity_date=date, customer_email=email, customer_phone=phone, activity_time=time)
    # Process the booking (e.g., save to a database)

    try:
        # Attempt to add the new User object to the database
        db.session.add(new_activity)
        # Commit the transaction
        db.session.commit()
        print('Details entered successfully!')
    except Exception as e:
        # If an error occurs, roll back the transaction
        db.session.rollback()
        print(e)
        print('An error occurred while booking the activity.')
    return f"Booking received for {name} to {activity} on {date} at {time}."




if __name__ == '__main__':
    app.run(debug=True)





#mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, email, phone, activity, date, time)"
#booking_sql = "INSERT INTO activity_bookings ()"
#mycursor.execute(sql)

#mydb.commit()

