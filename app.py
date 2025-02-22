from flask import Flask, render_template
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/')
def index():
    try:
        mydb = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'db'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE')
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT username, email FROM users")
        users = cursor.fetchall()
        cursor.execute("SELECT name, price FROM products")
        products = cursor.fetchall()
        return render_template('index.html', users=users, products=products)
    except mysql.connector.Error as err:
        return render_template('index.html', message=f"Error: {err}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')