from app import db

class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    location = db.Column(db.String)
    members = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            location=self.life,
            members=self.moons,
        )
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            description=data_dict["description"],
            location=data_dict["location"],
            members=data_dict["members"]
        )
    
    def replace_details(self, data_dict):
        self.name=data_dict["name"]
        self.description=data_dict["description"]
        self.life=data_dict["location"]
        self.moons=data_dict["members"]
    