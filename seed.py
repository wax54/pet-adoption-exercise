from models import db
from models.Pet import Pet

from app import app

db.drop_all()
db.create_all()


pets = [
    Pet(name='Clifford', species='Dog', age=3, notes="pulls on leash"),
    Pet(name='Strussel', species='Cat', age=5),
    Pet(name='Adam', species='Bunny'),
    Pet(name='Burger', species='Dog', available=False)
]


db.session.add_all(pets)
db.session.commit()
