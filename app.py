from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)

# Simulated VPN Server locations
SERVERS = {
    "US-EAST": "192.168.1.10 (Virginia, USA)",
    "EU-CENTRAL": "172.16.0.5 (Frankfurt, DE)",
    "ASIA-PACIFIC": "10.0.0.8 (Tokyo, JP)"
}

@app.route('/')
def home():
    return render_template('index.html', servers=SERVERS)

@app.route('/connect', methods=['POST'])
def connect_vpn():
    # Simulate the "Handshake" delay and encryption setup
    time.sleep(1.5) 
    data = request.json
    server_name = data.get('server')
    return jsonify({
        "status": "connected", 
        "message": f"Encrypted Tunnel Established to {server_name}",
        "new_ip": SERVERS.get(server_name)
    })

@app.route('/proxy', methods=['POST'])
def proxy_request():
    # This function acts as the VPN. It fetches the website FOR the user.
    # This hides the user's actual IP from the target site.
    target_url = request.json.get('url')
    
    if not target_url.startswith('http'):
        target_url = 'http://' + target_url

    try:
        # mimic a real browser user agent so websites don't block us
        headers = {'User-Agent': 'Mozilla/5.0 (VPN-Prototype)'}
        response = requests.get(target_url, headers=headers, timeout=5)
        
        # In a real VPN, we stream data. Here we just grab the text/status for the prototype.
        return jsonify({
            "status": "success",
            "code": response.status_code,
            "content_preview": response.text[:500] + "..." # Show first 500 chars
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)