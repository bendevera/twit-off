from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


app = Flask(__name__)
app_settings = os.getenv(
    'APP_SETTINGS',
    'server.config.ProductionConfig'
)
app.config.from_object(app_settings)

db = SQLAlchemy(app)
CORS(app)

import server.api