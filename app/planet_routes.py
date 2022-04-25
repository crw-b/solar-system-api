from flask import Blueprint, jsonify, abort, make_response

class Planet:
	def __init__(self, id, name, description, no_life=True):
		self.id = id
		self.name = name
		self.description = description
		self.no_life = no_life 

	def to_dict(self):
		return dict(
			id=self.id,
			name=self.name,
			description=self.description,
			no_life=self.no_life)


planets = [
    Planet(1, "Methuselah", "oldest exoplanet"),
    Planet(2, "Epsilon Eridani b", "closest exoplanet, has 2 astroid belts!!"),
    Planet(3, "Aquarii A", "the most suns!"),
    Planet(4, "Gliese 876 b", "gas giant, big, icy moons, water might be found", False)
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
							# ^ this , makes it a tuple! 
		#  ^ can leave blank cuz we already filled the method
def index_planets(): 
# we have our list of cat instances, but not a dictionary of their info! need to make a dictionary of cats 
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



