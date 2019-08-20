from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'IUY943FY987SENY8NSDIOFSIDUHFISFKNJ'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:baku2019@localhost:5432/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


db = SQLAlchemy(app)



