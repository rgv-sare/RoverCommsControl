from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake telemetry data
telemetry = {
    "temperature": 25,  # in degrees Celsius
    "battery_life": 87,  # in percentage
    "radiation": 5.4,  # in Gy
    "orientation": {
        "x": 12,
        "y": -7,
        "z": 53
    },
    "acceleration": {
        "x": 0.1,
        "y": 0.02,
        "z": 0.3
    }
}

# Route to return telemetry data
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify(telemetry)

# Route to receive commands
@app.route('/command', methods=['POST'])
def command():
    command_data = request.json
    # Here you could add code to handle the command data if needed
    return jsonify({"status": "acknowledged", "command_received": command_data})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
