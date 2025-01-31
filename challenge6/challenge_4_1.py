from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import socket
import os

# Initialize Flask application
app = Flask(__name__)

# MongoDB Client Initialization
mongo_url = os.getenv('MONGO_URL', 'mongodb://mongodb:27017/')
client = MongoClient(mongo_url)
db = client['mydatabase']
collection = db['mycollection']

@app.route("/")
def hello_world():
    
    # Get client IP address
    client_ip = request.remote_addr

    # Get current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert request details into MongoDB
    record = {"ip_address": client_ip, "date": current_date}
    collection.insert_one(record)

    # Retrieve the last 10 records
    last_records = collection.find().sort("_id", -1).limit(10)
    records_html = "<ul>"
    for record in last_records:
        records_html += f"<li>{record.get('ip_address')} - {record.get('date')}</li>"
    records_html += "</ul>"

    # Hostname and response
    hostname = socket.gethostname()
    return (
        f"<p>Name : Falilou</p>"
        f"<p>Project name : Challenge 3</p>"
        f"<p>Version : V2</p>"
        f"<p>Hostname : {hostname}</p>"
        f"<p>Current date : {current_date}</p>"
        f"<p>Client IP : {client_ip}</p>"
        f"<p>Last 10 records : {records_html}</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
