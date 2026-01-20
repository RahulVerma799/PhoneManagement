from flask import Flask
from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from models.contact_Schema import contact_Schema
from routes.contact_routes import contact_bp
from flask_cors import CORS

from config.config import db 


# Flask app



app = Flask(__name__)
app.secret_key = "secret123"
CORS(app)

# Register blueprint
app.register_blueprint(contact_bp)

# Simple home route
@app.route('/')
def home():
    return jsonify({'message': 'Phonebook API', 'status': 'running'})

if __name__ == "__main__":
    app.run(debug=True)
