from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SINGHA@ronit@011002",
        database="HotelReservation"
    )

# Book a Room API
@app.route("/book_room", methods=["POST"])
def book_room():
    data = request.json
    guest_id = data["guest_id"]
    room_id = data["room_id"]
    check_in = data["check_in"]
    check_out = data["check_out"]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Reservations (guest_id, room_id, check_in, check_out, status) VALUES (%s, %s, %s, %s, 'Confirmed')", (guest_id, room_id, check_in, check_out))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Room Booked Successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
