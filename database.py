from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'reviews_db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    review = db.Column(db.String(40), nullable=False)




    def __init__(self, name, date, rating,review ):
        self.name = name
        self.date = date
        self.rating = rating
        self.review = review

@app.route('/')
def index():
    print("in index")
    #return render_template('index.html')
    return render_template('reviews.html')

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

@app.route('/submit_review', methods=['GET','POST'])
def submit_review():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        rating = request.form.get('rating')
        review = request.form.get('review')

        new_message = Reviews(name=name, date=date, rating=rating, review=review)
        db.session.add(new_message)
        db.session.commit()
    # Process the booking (e.g., save to a database)
    return render_template('reviews.html')





if __name__ == '__main__':
    app.run(debug=True)