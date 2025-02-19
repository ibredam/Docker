# app.py
from flask import Flask, render_template
from flask_mysqldb import MySQL
from database_config import db_config

app = Flask(__name__)

app.config['MYSQL_HOST'] = db_config['host']
app.config['MYSQL_USER'] = db_config['user']
app.config['MYSQL_PASSWORD'] = db_config['password']
app.config['MYSQL_DB'] = db_config['database']

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data) # Pass data to the template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)