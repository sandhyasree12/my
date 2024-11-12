from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to the System Information App</h1>
    <p>Visit <a href='/htop'>/htop</a> for system information.</p>
    """

@app.route('/htop')
def htop():
    # Define your full name
    name = "Pujali Sandhya Sree"  
    
    # Get the system username (checks multiple environment variables)
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    
    # Get the current server time in IST (Indian Standard Time)
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " IST"

    # Run the 'top' command in batch mode to capture output
    top_output = subprocess.getoutput("top -b -n 1")

    # Create the HTML response with the required data
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

