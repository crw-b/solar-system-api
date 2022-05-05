from xml.dom.minidom import Identified
from app import db
from app.models.galaxy import Galaxy
from flask import Blueprint, jsonify, make_response, request, abort 
from app.routes.routes_helper import error_message


galaxy_bp = Blueprint("galaxys", __name__, url_prefix="/galaxys")

def make_galaxy_safely(data_dict):
	try:
		return Galaxy.from_dict(data_dict)
	except KeyError as err:
		error_message(f"Missing key: {err}", 400)

def replace_galaxy_safely(galaxy, data_dict):
	try:
		galaxy.replace_details(data_dict)
	except KeyError as err:
		error_message(f"Missing key: {err}", 400)

@galaxy_bp.route("", methods=["POST"])
def handle_galaxys():
	request_body = request.get_json()
	# new_galaxy = Galaxy(
	# 	name=request_body["name"],
	# 	description=request_body["description"],
	# 	life = request_body["life"],
	# 	moons = request_body["moons"])
	new_galaxy = make_galaxy_safely(request_body)

	db.session.add(new_galaxy)
	db.session.commit()

	return jsonify(new_galaxy.to_dict()), 201

@galaxy_bp.route("", methods=["GET"])
def index_galaxys(): 
	# galaxys = Galaxy.query.all()
	name_param = request.args.get("name")

	if name_param:
		galaxys = Galaxy.query.filter_by(name=name_param)
	else:
		galaxys = Galaxy.query.all()

	result_list = [galaxy.to_dict() for galaxy in galaxys]
	return jsonify(result_list) 

@galaxy_bp.route("/<id>", methods=["GET"])
def get_galaxy(id):
	galaxy = validate_galaxy(id) 
	return jsonify(galaxy.to_dict())


def validate_galaxy(id):
	try:
		id = int(id)
	except ValueError:
		# abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))
		error_message(f"Invalid id {id}", 400)

	galaxy = Galaxy.query.get(id)
		
	if galaxy:
		# abort(make_response(jsonify(dict(details=f"galaxy id {id} not found")), 404))
		return galaxy
	error_message(f"No galaxy with id {id} found", 404)

@galaxy_bp.route("/<id>", methods=["PUT"])
def update_galaxy(id): 
	galaxy = validate_galaxy(id)
	request_body = request.get_json()
	galaxy.name = request_body['name']
	galaxy.location = request_body['location']
	galaxy.members = request_body['members']
	  
	db.session.commit()
	return jsonify(galaxy.to_dict())

@galaxy_bp.route("/<id>", methods=["DELETE"])
def delete_galaxy(id): 
	galaxy = validate_galaxy(id)
	db.session.delete(galaxy)
	db.session.commit()
	return make_response(f'*** You have successfully destroyed {galaxy.name} ! *** ')







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

    Galaxy(2, "Epsilon Eridani", 10.5, galaxys, ),
    
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

