from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'contact.db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False)
    message = db.Column(db.String(40), nullable=False)



def __init__(self,email,message):
    self.email = email
    self.message = message

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

@app.route('/contact', methods=['POST'])
def submit_booking():
    message = request.form['message']
    email = request.form['email']
    new_message = Message(email=email, message=message)
    # Process the booking (e.g., save to a database)

    try:
        # Attempt to add the new User object to the database
        db.session.add(new_message)
        # Commit the transaction
        db.session.commit()
        print('message entered successfully!')
    except Exception as e:
        # If an error occurs, roll back the transaction
        db.session.rollback()
        print(e)
        print('An error occurred while booking the activity.')
    return f"Message received from {email}."




if __name__ == '__main__':
    app.run(debug=True)