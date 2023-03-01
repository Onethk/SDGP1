from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sdgp'


mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('testo.html')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        feedback = request.form['feedback']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO testimonials (feedback) VALUES (%s)", (feedback,))
        mysql.connection.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
