import datetime as datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# secret key given to display the flash
app.secret_key = "Feedback message"

# database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sdgp'


mysql = MySQL(app)


@app.route('/')
def index():

    # Retrieving data from the database
    cur = mysql.connection.cursor()
    # Selects the feedback randomly and limits the number of feedback to be displayed as 5
    cur.execute("SELECT * FROM testimonials ORDER BY RAND() LIMIT 5")
    data = cur.fetchall()
    cur.close()

    return render_template('testo.html', testimonials=data)


# Insert the User's name, feedback and date into database
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        # Flashing a message
        flash("Your feedback is successfully stored, Thank you for the feedback :)")

        first_name = request.form['fName']
        surname = request.form['sName']
        feedback = request.form['feedback']
        rating = request.form['rating']
        date = datetime.date.today()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO testimonials (firstname, surname, feedback, starRating, date) VALUES (%s, %s, %s, %s, %s)",
                    (first_name, surname, feedback, rating, date,))
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
