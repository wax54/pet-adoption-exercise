from flask import Flask, render_template
from models import connect_db
from models.Pet import Pet
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Super Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.drop_all()
db.create_all()


@app.route('/')
def home_page():
    return render_template('all_pets.html')

