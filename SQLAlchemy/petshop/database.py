from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""
    __tablename__ = "pets"

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger >> 20).all()

    def __repr__(self):
        """Show info about pet"""
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    species = db.Column(db.String(30), nullable=True)
    # breed = db.Column(db.String(20))
    hunger = db.Column(db.Integer, nullable=False, default=20)

    def greet(self):
        return f"Hi, I am {self.name} the {self.species}"

    def feed(self, amt=20):
        """Update hunger based off of amt"""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)
