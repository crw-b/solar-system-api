from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    life = db.Column(db.Boolean)
    moons = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            life=self.life,
            moons=self.moons,
        )
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            description=data_dict["description"],
            life=data_dict["life"],
            moons=data_dict["moons"]
        )
    
    def replace_details(self, data_dict):
        self.name=data_dict["name"]
        self.description=data_dict["description"]
        self.life=data_dict["life"]
        self.moons=data_dict["moons"]
        return self.to_dict()
