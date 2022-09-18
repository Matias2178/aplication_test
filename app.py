"""
Autor: Matias Martelossi
Creation: 17/09/2022
"""

from flask import Flask
from flask_migrate import Migrate
from database import db
import os
from dotenv import load_dotenv


app = Flask(__name__)

# db Configuration load in .env file
load_dotenv()
USER_DB = os.getenv('ENV_USER_DB')
PASS_DB = os.getenv('ENV_PASS_DB')
URL_DB = os.getenv('ENV_URL_DB')
NAME_DB = os.getenv('ENV_NAME_DB')
SECRETS_KEY = os.getenv('ENV_SECRETS_KEY')

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

# Config flask migrate
migrate = Migrate()
migrate.init_app(app, db)




