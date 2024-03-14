# RoverCommsControl

![Space Cowboy](https://github.com/rgv-sare/RoverCommsControl/blob/main/SpaceCowboyCommsCenter.webp "See You Space Cowboy!")

## Overview
RoverCommsControl is a Flask-based server designed to manage telemetry data and command interfaces for rovers. It enables real-time data access and control, facilitating remote operations and monitoring.

## Features
- **Telemetry Data Access**: Provides access to real-time telemetry data from the rover.
- **Command Interface**: Allows the sending of operational commands to the rover for remote control.
- **JSON API**: Utilizes JSON for easy integration with clients and third-party services.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Any modern web browser or API testing tool (e.g., Postman, Thunder Client).

### Installation
1. Clone the repository to your local machine:
   https://github.com/rgv-sare/RoverCommsControl.git
   
2. Navigate to the cloned directory:
   cd RoverCommsControl

3. Install the required Python packages:
   pip install -r requirements.txt


### Running the Server
Execute the following command to start the Flask server:
python app.py

The server will start on `http://localhost:5000`. **Adjust the host and port as needed based on your environment and preferences.**

## Usage
- Access telemetry data: Navigate to `http://localhost:5000/telemetry` in your web browser or use an API testing tool to view the telemetry data.
- Send commands to the rover: Use an API testing tool to send POST requests to `http://localhost:5000/command` with appropriate JSON payload.

## Contributing
We welcome contributions! Please feel free to fork the repository and submit pull requests with any enhancements, bug fixes, or improvements.

## License
RoverCommsControl is open-source software licensed under the [MIT license](LICENSE).

## Acknowledgments
- NASA Minds for the opportunity to contribute to rover communications and control.
- Flask community for the support.


