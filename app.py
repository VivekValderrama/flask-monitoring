from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.INFO,   # Log level (INFO, ERROR, DEBUG, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return jsonify({"message": "Welcome to Flask Logging API!"})

@app.route('/error')
def error():
    app.logger.error("Error route accessed")
    return jsonify({"error": "This is a test error!"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
