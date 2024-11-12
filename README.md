# my
System Information Flask App
This is a simple Flask-based web application that displays system information including the full name, system username, server time in IST, and the output of the top command. This application is designed to provide a quick view of system stats in a user-friendly web interface.

Features
Displays System Information:

Full name (customizable).
System username (automatically fetched from environment variables).
Current server time in IST (Indian Standard Time).
Top output showing the current processes and resource usage.
Web Interface:

Access the system information through a web page served by Flask.

Install Dependencies: Ensure you have Python installed. If Flask is not installed, you can install it using pip:

pip install flask
Run the Flask App: In the project directory, run the Flask app with:


python app.py
Access the Application: Open your web browser in an incognito window and visit:

url: http://localhost:5000/htop
This will display the system information on the webpage.

Endpoints
/: Displays a welcome message and a link to the /htop endpoint.
/htop: Displays the system information including:
Full Name: Your name.
Username: The system username.
Server Time: Current server time in IST.
Top Output: System resource usage and processes.
Example Output is provided as output.png
When you access /htop, you will see something like this:

Name: Pujali Sandhya Sree
Username: sandhyasree12
Server Time: 2024-11-12 12:30:45 IST

Top Output:
------------------------------
Processes running on the system...
CPU usage, memory usage, etc.
------------------------------
License
This project is open source and available under the MIT License.
