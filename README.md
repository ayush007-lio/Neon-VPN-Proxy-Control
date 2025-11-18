🌟 Project Title: Neon VPN Proxy Control
    A prototype web interface for a Secure Cloud Access / VPN system, featuring a retro-futuristic, neon-hacked aesthetic. This project simulates the core functions of a VPN client: connection, server selection, and proxying web requests to demonstrate the concept of IP obfuscation.

<img width="1794" height="830" alt="Screenshot (22)" src="https://github.com/user-attachments/assets/ae09bdfe-b3d0-4627-a01e-0f620157ea4a" />

  ✨ Key Features
      Cyberpunk Aesthetic: A responsive, dark-mode design with glowing neon accents using pure HTML/CSS.
      
      Connection Simulation: A toggle button and status indicator simulate the VPN handshake and tunnel activation process with a 1.5-second delay.
      
      Server Selection: Allows selection of simulated remote server locations (US, EU, ASIA).
      
      Web Proxy Functionality: Uses a Flask backend and the requests library to fetch a requested URL, acting as the secure middleman (the "VPN tunnel").
      
      Terminal Output: Real-time log output tracks connection status, IP address assignment, and proxy request results.  

  Category,Technology,Purpose
    Backend,Python (Flask),"Handling server logic, routing, and making external web requests (proxy)."
    Frontend,"HTML5, CSS3, JavaScript (Vanilla JS)","Building the user interface and handling front-end interactions (e.g., button clicks, logging)."
    Libraries,Python requests,Used in app.py to perform the actual web-fetching for the proxy. 

🚀 Project Workflow (End-to-End Detail)
      Initial Load (app.py -> index.html):
      
      The Flask application starts and serves the index.html template.
      
      The app.py populates the Server Selection dropdown using the SERVERS dictionary.
      
      Connection Initialization (Frontend):
      
      The user selects a server (e.g., US-EAST) and clicks "Initialize Uplink."
      
      The toggleConnection() JavaScript function sends a POST request to the /connect endpoint in app.py.
      
      Backend Handshake Simulation (app.py):
      
      The /connect route intentionally uses time.sleep(1.5) to simulate the network latency and "handshake" process of establishing a secure tunnel.
      
      It responds with a JSON object containing "status": "connected" and a simulated new_ip.
      
      Secure Tunnel Active (Frontend):
      
      The toggleConnection() function updates the UI: the status dot turns neon-blue, the text changes to "SECURE TUNNEL ACTIVE," and the connection button changes to "Terminate Connection."
      
      The Secure Browser input and button are now enabled.
      
      Proxy Request (fetchUrl()):
      
      The user enters a URL and clicks "Access URL."
      
      The fetchUrl() JavaScript function sends a POST request to the /proxy endpoint in app.py, passing the target URL.
      
      Backend Proxy Action (app.py):
      
      The /proxy route uses the requests.get() function to fetch the external URL from the Flask server's perspective.
      
      This is the core concept: the target website sees the IP address of the Flask server (the VPN), not the user's actual IP.
      
      It returns a JSON response with a status code and a content preview.
      
      Data Reception (Frontend):
      
      The UI logs the status code and displays the content preview in the terminal, simulating the secure reception of data. 

How to Run Locally
      To get this prototype running on your machine:
      
      Clone the repository:
      
      Bash
      
      git clone [Your Repository URL]
      cd [Your Repository Name]
      Set up the Python Environment:
      
      Bash
      
      # Install Flask and requests
      pip install flask requests
      Run the Flask Application:
      
      Bash
      
      python app.py
      Access the App:
      
      Open your web browser and navigate to http://127.0.0.1:5000 (or http://localhost:5000).
