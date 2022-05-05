from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request
from app.routes.routes_helper import error_message

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def make_planet_safely(data_dict):
	try:
		return Planet.from_dict(data_dict)
	except KeyError as err:
		error_message(f"Missing key: {err}", 400)

def replace_planet_safely(planet, data_dict):
	try:
		planet.replace_details(data_dict)
	except KeyError as err:
		error_message(f"Missing key: {err}", 400)

@planets_bp.route("", methods=["POST"])
def handle_planets():
	request_body = request.get_json()
	new_planet = make_planet_safely(request_body)

	db.session.add(new_planet)
	db.session.commit()

	return jsonify(new_planet.to_dict()), 201

@planets_bp.route("", methods=["GET"])
def index_planets(): 
	name_param = request.args.get("name")

	if name_param:
		planets = Planet.query.filter_by(name=name_param)
	else:
		planets = Planet.query.all()

	result_list = [planet.to_dict() for planet in planets]
	return jsonify(result_list) 

@planets_bp.route("/<id>", methods=["GET"])
def get_planet(id):
	planet = validate_planet(id) 
	return jsonify(planet.to_dict())

def validate_planet(id):
	try:
		id = int(id)
	except ValueError:
		error_message(f"Invalid id {id}", 400)

	planet = Planet.query.get(id)
		
	if planet:
		return planet
	error_message(f'No planet with id {id} found', 404)

@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id): 
	planet = validate_planet(id)
	request_body = request.get_json()
	planet.name = request_body['name']
	planet.description = request_body['description']
	planet.life = request_body['life']
	planet.moons = request_body['moons']
	db.session.commit()
	return jsonify(planet.to_dict())

@planets_bp.route("/<id>", methods=["PATCH"])
def upgrade_planet_with_id(id):
    planet = validate_planet(id)
    request_body = request.get_json()
    planet_keys = request_body.keys()

    if "name" in planet_keys:
        planet.name = request_body["name"]
    if "description" in planet_keys:
        planet.description = request_body["description"]
    if "life" in planet_keys:
        planet.life = request_body["life"]



    db.session.commit()
    return jsonify(planet.to_dict())




@planets_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id): 
	planet = validate_planet(id)
	db.session.delete(planet)
	db.session.commit()
	return make_response('*** You have successfully destroyed Earth ! ***')