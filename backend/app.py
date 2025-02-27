from flask import Flask, render_template, json, redirect, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_leebr8'
app.config['MYSQL_PASSWORD'] = '4358'
app.config['MYSQL_DB'] = 'cs340_leebr8'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Default route
@app.route('/')
def root():
    return render_template("main.j2")

# RETRIEVE ALL ROWS
@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users;")
    users = cur.fetchall()
    cur.close()
    return {'users': users}, 200

# GET
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE user_id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user if user else {}, 200

# POST
@app.route('/users/insert', methods=['POST'])
def create_user():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Users (first_name, last_name, email, phone_number, creation_date)
        VALUES (%s, %s, %s, %s, %s);
    """, (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['creation_date']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'User added successfully'}, 201

# PUT
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Users
        SET first_name=%s, last_name=%s, email=%s, phone_number=%s, creation_date=%s
        WHERE user_id=%s;
    """, (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['creation_date'], user_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'User updated successfully'}, 200

# DELETE
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Users WHERE user_id = %s;", (user_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'User deleted successfully'}, 200

# Listener
if __name__ == "__main__":
    app.run(port=3851, debug=True)