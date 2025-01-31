from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    
    name = "Fodé DIOUF" 
    project_name = "Challenge1"
    version = "V1"
    hostname = request.host  
    date = "10/11/2024" 

    # Contenu HTML
    html_content = f"""
    <html>
        <head>
            <title>{project_name}</title>
        </head>
        <body>
            <h1>{project_name}</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Version:</strong> {version}</p>
            <p><strong>Server Hostname:</strong> {hostname}</p>
            <p><strong>Current Date:</strong> {date}</p>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
