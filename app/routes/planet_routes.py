from flask import Blueprint, jsonify, abort, make_response

class Planet:
	def __init__(self, id, name, description, moons=None, life=True):
		self.id = id
		self.name = name
		self.description = description
		self.life = life 
		self.moons = moons if moons is not None else []

	def to_dict(self):
		return dict(
			id=self.id,
			name=self.name,
			description=self.description,
			life=self.life,
			moons = self.moons)


planets = [
    Planet(1, "Epsilon Eridani I ", "closest planet to the star", life=False),
    Planet(2, "Epsilon Eridani II", "2 astroid belts, most developed human colony", ["Turul", "Csodaszarvas"]),
    Planet(3, "Epsilon Eridani III", "aka Tribute", ["Emese"]),
    Planet(4, "Circumstance", "world-famous")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
						
def index_planets(): 
	result_list = [planet.to_dict() for planet in planets]

	return jsonify(result_list) 

def validate_planet(id):
	try:
		id = int(id)
	except ValueError:
		abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))
	
	for planet in planets:
		if planet.id == id:
			return planet
	
	abort(make_response(jsonify(dict(details=f"planet id {id} not found")), 404))


@bp.route("/<id>", methods=["GET"])
def get_planet(id): 
	planet = validate_planet(id)
	return jsonify(planet.to_dict())



