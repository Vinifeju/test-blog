# == Main App File ==

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import AppConfig
from register.register import register_blueprint

app = Flask(__name__)
app.config.from_object(AppConfig)
db = SQLAlchemy(app)
app.url_map.strict_slashes = False

# === Blueprints
app.register_blueprint(register_blueprint, url_prefix='/register')

import views
