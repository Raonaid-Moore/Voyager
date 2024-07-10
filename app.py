from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    activity = request.form['activity']
    date = request.form['date']
    time = request.form['time']
    # Process the booking (e.g., save to a database)
    return f"Booking received for {name} to {activity} on {date} at {time}."

if __name__ == '__main__':
    app.run(debug=True)
