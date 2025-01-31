from flask import Flask, request, render_template
from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime
import socket
import os

app = Flask(__name__)

# Connexion à MongoDB
monfo_url=os.getenv('MONGO_URL', 'mongodb://mongodb:27017/')
client = MongoClient()  # Utilise le nom du service Docker Compose
db = client["flask_db"]
collection = db["requests"]

@app.route('/')
def index():
    # Récupérer les informations demandées
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Enregistrer la requête dans MongoDB
    client_ip = request.remote_addr
    collection.insert_one({
        "ip": client_ip,
        "date": current_date
    })

    # Récupérer les 10 derniers enregistrements
    last_records = list(collection.find().sort("_id", -1).limit(10))

    # Afficher les informations
    return render_template('index.html', 
                           name="DIOUF FODE", 
                           project_name="CHALLENGE3", 
                           version="V2", 
                           hostname=hostname, 
                           current_date=current_date, 
                           last_records=last_records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)