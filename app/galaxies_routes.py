from flask import Blueprint, jsonify, abort, make_response
from planet_routes import Planet, planets

class Galaxy:
	def __init__(self, id, name, location, members=None):
		self.id = id
		self.name = name
		self.location = (f'{location} light-years')
		self.members = members if members is not None else []


	def to_dict(self):
		return dict(
			id=self.id,
			name=self.name,
			location = self.location,
			members = self.members)


galaxies = [

    Galaxy(2, "Epsilon Eridani", 10.5, planets, ),
    
]


galaxy_bp = Blueprint("galaxies", __name__, url_prefix="/galaxies")

@galaxy_bp.route("", methods=["GET"])
						
def index_galaxies(): 
	result_list = [galaxy.to_dict() for galaxy in galaxies]

	return jsonify(result_list) 

def validate_galaxy(id):
	try:
		id = int(id)
	except ValueError:
		abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))
	
	for galaxy in galaxies:
		if galaxy.id == id:
			return galaxy
	
	abort(make_response(jsonify(dict(details=f"galaxy id {id} not found")), 404))


@galaxy_bp.route("/<id>", methods=["GET"])
def get_galaxy(id): 
	galaxy = validate_galaxy(id)
	return jsonify(galaxy.to_dict())

