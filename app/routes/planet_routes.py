from xml.dom.minidom import Identified
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort 

# class Planet:
# 	def __init__(self, id, name, description, no_life=True):
# 		self.id = id
# 		self.name = name
# 		self.description = description
# 		self.no_life = no_life 

# 	def to_dict(self):
# 		return dict(
# 			id=self.id,
# 			name=self.name,
# 			description=self.description,
# 			no_life=self.no_life)


# planets = [
#     Planet(1, "Methuselah", "oldest exoplanet"),
#     Planet(2, "Epsilon Eridani b", "closest exoplanet, has 2 astroid belts!!"),
#     Planet(3, "Aquarii A", "the most suns!"),
#     Planet(4, "Gliese 876 b", "gas giant, big, icy moons, water might be found", False)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planets():
	request_body = request.get_json()
	new_planet = Planet(
		name=request_body["name"],
		description=request_body["description"],
		life = request_body["life"],
		moons = request_body["moons"])

	db.session.add(new_planet)
	db.session.commit()

	return jsonify(new_planet.to_dict()), 201

@planets_bp.route("", methods=["GET"])
def index_planets(): 
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
		abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))
	

	planet = Planet.query.get(id)
		
	if not planet:
		abort(make_response(jsonify(dict(details=f"planet id {id} not found")), 404))
	return planet


# @bp.route("/<id>", methods=["GET"])
# def get_planet(id): 
# 	planet = validate_planet(id)
# 	return jsonify(planet.to_dict())



