from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    email = request.form['email']
    select_room = request.form['select room']
    check_in= request.form['check in']
    check_out = request.form['check out']
    # Process the booking (e.g., save to a database)
    return f"Booking received for {email} to {select_room} on {check_in} on {check_out}."

if __name__ == '__main__':
    app.run(debug=True)
