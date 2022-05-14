from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://jrvixwqhuhbxvs:5be4ce4d3678ca86710ae4cd99b364441518d43beb88dfd70043eaa8470a5768@ec2-52-73-155-171.compute-1.amazonaws.com:5432/dfd71pcvfm3p6v'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()
    db.close()
    