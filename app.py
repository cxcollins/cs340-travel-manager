from flask import Flask, render_template, json, redirect, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure MySQL using environment variables
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = os.getenv('MYSQL_CURSORCLASS')

mysql = MySQL(app)

# ROUTES TO RENDER HTML PAGES
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/users')
def users():
    return render_template("users.html")

@app.route('/travel_plans')
def travel_plans():
    return render_template("travel_plans.html")

@app.route('/destinations')
def destinations():
    return render_template("destinations.html")

@app.route('/hotels')
def hotels():
    return render_template("hotels.html")

@app.route('/activities')
def activities():
    return render_template("activities.html")

@app.route('/destinations_activities')
def destinations_activities():
    return render_template("destinations_activities.html")

# FETCH ALL USERS
@app.route('/users/fetchall', methods=['GET'])
def fetchall_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users;")
    users = cur.fetchall()
    cur.close()
    return {'users': users}, 200

# GET USER
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE user_id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user if user else {}, 200

# INSERT USER
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

# UPDATE USER
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

# DELETE USER
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Users WHERE user_id = %s;", (user_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'User deleted successfully'}, 200

# FETCH ALL DESTINATIONS
@app.route('/destinations/fetchall', methods=['GET'])
def fetchall_destinations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Destinations;")
    destinations = cur.fetchall()
    cur.close()
    return {'destinations': destinations}, 200

# GET DESTINATION
@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Destinations WHERE destination_id = %s;", (destination_id,))
    destination = cur.fetchone()
    cur.close()
    if destination:
        return destination, 200
    else:
        return {'message': 'Destination not found'}, 404

# UPDATE DESTINATION
@app.route('/destinations/update/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Destinations
        SET country=%s, state=%s, city=%s
        WHERE destination_id=%s;
    """, (data['country'], data['state'], data['city'], destination_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destination updated successfully'}, 200

# DELETE DESTINATION
@app.route('/destinations/delete/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM Destinations
                WHERE destination_id = %s;
    """, (destination_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destination deleted successfully'}, 200

# INSERT DESTINATION
@app.route('/destinations/insert', methods=['POST'])
def create_destination():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Destinations (country, state, city)
        VALUES (%s, %s, %s);
    """, (data['country'], data['state'], data['city']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destinations added successfully'}, 201

# FETCH ALL ACTIVITIES
@app.route('/activities/fetchall', methods=['GET'])
def fetchall_activities():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Activities;")
    activities = cur.fetchall()
    cur.close()
    return {'activities': activities}, 200

# UPDATE ACTIVITY
@app.route('/activities/update/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Activities
        SET name=%s, type=%s
        WHERE activity_id=%s;
    """, (data['name'], data['type'], activity_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Activity updated successfully'}, 200

# DELETE ACTIVITY
@app.route('/activities/delete/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM Activities
                WHERE activity_id = %s;
    """, (activity_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Activity deleted successfully'}, 200

# INSERT ACTIVITY
@app.route('/activities/insert', methods=['POST'])
def create_activity():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Activities (name, type)
        VALUES (%s, %s);
    """, (data['name'], data['type']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Activity added successfully'}, 201

# FETCH ALL DESTINATIONS ACTIVITIES
@app.route('/destinations_activities/fetchall', methods=['GET'])
def fetchall_destinations_activities():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Destinations_Activities;")
    destinations_activities = cur.fetchall()
    cur.close()
    return {'destinations_activities': destinations_activities}, 200

# INSERT DESTINATION ACTIVITY
@app.route('/destinations_activities/insert', methods=['POST'])
def create_destination_activity():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Destinations_Activities (destination_id, activity_id)
        VALUES (%s, %s);
    """, (data['destination_id'], data['activity_id']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destination Activity added successfully'}, 201

# UPDATE DESTINATION ACTIVITY
@app.route('/destinations_activities/update/<int:destination_activity_id>', methods=['PUT'])
def update_destination_activity(destination_activity_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Destinations_Activities
        SET destination_id=%s, activity_id=%s
        WHERE destination_activity_id=%s;
    """, (data['destination_id'], data['activity_id'], destination_activity_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destination Activity updated successfully'}, 200

# DELETE DESTINATION ACTIVITY
@app.route('/destinations_activities/delete/<int:destination_activity_id>', methods=['DELETE'])
def delete_destination_activity(destination_activity_id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM Destinations_Activities
                WHERE destination_activity_id = %s;
    """, (destination_activity_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Destination Activity deleted successfully'}, 200

# FETCH ALL TRAVEL PLANS
@app.route('/travel_plans/fetchall', methods=['GET'])
def fetchall_travel_plans():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Travel_Plans;")
    travel_plans = cur.fetchall()
    cur.close()
    return {'travel_plans': travel_plans}, 200

# INSERT TRAVEL PLAN
@app.route('/travel_plans/insert', methods=['POST'])
def create_travel_plan():
    data = request.json
    cur = mysql.connection.cursor()
    nullableDestinationId = data.get('destination_id')
    cur.execute("""
        INSERT INTO Travel_Plans (user_id, destination_id, start_date, end_date, budget, status)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (data['user_id'], nullableDestinationId, data['start_date'], data['end_date'], data['budget'], data['status']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Travel Plan added successfully'}, 201

# UPDATE Travel Plan
@app.route('/travel_plans/update/<int:plan_id>', methods=['PUT'])
def update_travel_plan(plan_id):
    data = request.json
    cur = mysql.connection.cursor()
    nullableDestinationId = data.get('destination_id')
    cur.execute("""
        UPDATE Travel_Plans
        SET user_id=%s, destination_id=%s, start_date=%s, end_date=%s, budget=%s, status=%s
        WHERE plan_id=%s;
    """, (data['user_id'], nullableDestinationId, data['start_date'], data['end_date'], data['budget'], data['status'], plan_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Travel Plan updated successfully'}, 200

# DELETE Travel Plan
@app.route('/travel_plans/delete/<int:plan_id>', methods=['DELETE'])
def delete_travel_plan(plan_id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM Travel_Plans
                WHERE plan_id = %s;
    """, (plan_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Travel Plan deleted successfully'}, 200

# FETCH ALL HOTELS
@app.route('/hotels/fetchall', methods=['GET'])
def fetchall_hotels():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Hotels;")
    hotels = cur.fetchall()
    cur.close()
    return {'hotels': hotels}, 200

# INSERT HOTEL
@app.route('/hotels/insert', methods=['POST'])
def create_hotel():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Hotels (name, cost_per_night, rating, destination_id)
        VALUES (%s, %s, %s, %s);
    """, (data['name'], data['cost_per_night'], data['rating'], data['destination_id']))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Hotel added successfully'}, 201

# UPDATE HOTEL
@app.route('/hotels/update/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE Hotels
        SET name=%s, cost_per_night=%s, rating=%s, destination_id=%s
        WHERE hotel_id=%s;
    """, (data['name'], data['cost_per_night'], data['rating'], data['destination_id'], hotel_id))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Hotel updated successfully'}, 200

# DELETE HOTEL
@app.route('/hotels/delete/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Hotels WHERE hotel_id = %s;", (hotel_id,))
    mysql.connection.commit()
    cur.close()
    return {'message': 'Hotel deleted successfully'}, 200

# Listener
if __name__ == "__main__":
    app.run(port=35643, debug=True)