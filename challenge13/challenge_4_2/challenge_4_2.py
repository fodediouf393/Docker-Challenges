from flask import Flask, request
from datetime import datetime
import socket

# Initialize Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
    
    # Get client IP address
    client_ip = request.remote_addr

    # Get current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Hostname and response
    hostname = socket.gethostname()
    return (
        f"<p>Name : Fodé</p>"
        f"<p>Project name : Challenge 3</p>"
        f"<p>Version : V3</p>"  # Mise à jour de la version
        f"<p>Hostname : {hostname}</p>"
        f"<p>Current date : {current_date}</p>"
        f"<p>Client IP : {client_ip}</p>"
        f"<p>No MongoDB logs for this application</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
