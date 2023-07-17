from flask import (Blueprint, render_template)
import json

pet_data = json.load(open('pets.json'))

bp = Blueprint("pet", __name__, url_prefix="/pets")

# pets index route


@bp.route('/')
def index():
    return render_template('index.html', pets=pet_data)


@bp.route('/<int:index>')
def pet_view(index):
    found_pet = pet_data[index]
    return render_template('pet-show.html', pet=found_pet)
