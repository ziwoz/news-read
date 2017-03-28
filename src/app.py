from flask import Flask
from flask import render_template

from src.common.database import Database
from src.models.headlines.views import headlines_blueprint

app= Flask(__name__)
app.config.DEBUG = True

app.secret_key = "123"

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(headlines_blueprint, url_prefix="/headlines")
