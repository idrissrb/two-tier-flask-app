from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    cursor.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    msg = request.form.get('message')
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (%s)', (msg,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'status': 'Message added!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
