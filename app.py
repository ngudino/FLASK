from flask import Flask
from dbMySQL import DataBase
from flask_cors import CORS


#Creacion de la aplicacion
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS_HEADERS = 'Content-Type'
CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS_METHODS = ['GET', 'POST', 'DELETE', 'PUT', 'OPTIONS', 'HEAD']
