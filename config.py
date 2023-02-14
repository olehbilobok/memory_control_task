from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'memory_control',
    'host': 'test_mongodb',
    'username': 'root',
    'port': 27017,
    'password': 'pass',
    'authSource': 'admin'
}

db = MongoEngine()
db.init_app(app)
