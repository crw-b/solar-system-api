from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, no_life=True):
        self.id = id
        self.name = name
        self.description = description
        self.no_life = no_life 


planets = [
    Planet(1, "Methuselah", "oldest exoplanet"),
    Planet(2, "Epsilon Eridani b", "closest exoplanet, has 2 astroid belts!!"),
    Planet(3, "Aquarii A", "the most suns!"),
    Planet(4, "Gliese 876 b", "gas giant, big, icy moons, water might be found", False)


]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"],)
							# ^ this , makes it a tuple! 
		#  ^ can leave blank cuz we already filled the method
def index_planets(): 
# we have our list of cat instances, but not a dictionary of their info! need to make a dictionary of cats 
	all_planets = [] 
	for planet in planets: 
		all_planets.append(dict(
			id = planet.id,
			name = planet.name,
			description = planet.description, 
			no_life = planet.no_life,
))

	return jsonify(all_planets) 




