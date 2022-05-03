from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    life = db.Column(db.String)
    moons = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            life=self.life,
            moons=self.moons,
        )