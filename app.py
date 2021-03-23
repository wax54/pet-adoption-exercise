from flask import Flask, render_template, request, redirect
from models import connect_db
from models.Pet import Pet
from forms.Pet_Forms import NewPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Super Secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def home_page():
    """ Displays the Homepage"""
    pets = Pet.get_all()
    return render_template('pets_all.html', pets=pets)


@app.route('/add', methods=["POST", "GET"])
def add_new_pet():
    form = NewPetForm()
    if form.validate_on_submit():
        new_pet = Pet()
        form.populate_obj(new_pet)
        new_pet.update_db()
        return redirect('/')
    else:
        return render_template('pet_new_form.html', form=form)


@app.route('/<int:pet_id>', methods=["POST", "GET"])
def describe_pet(pet_id):
    pet = Pet.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        pet.update_db()
        return redirect('/')
    else:
        return render_template('pet_display.html', form=form, pet=pet)




