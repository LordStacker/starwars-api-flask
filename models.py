from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable =False)
    password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    isActive = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'isActive': self.isActive,
        }
    def serialize_just_username(self):
        return {
            'id': self.id,
            'name': self.name
        }
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Columndb.String(250), nullable=False)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String (250))
    crew = db.Column (db.Integer)
    manufacturer = db.Column(db.String(250))
    cargo_capacity = db.Column(db.Integer)
    cost_in_credits = db.Column(db.Integer)
    consumables = db.Column(db.Integer)

    def __repr__(self):
        return "<Vehicles %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.password,
            'crew': self.email,
            'consumables': self.isActive,
        }

class Characters(Base):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))


class Planets(Base):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(250))



class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False, primary_key=True)
    id_fav = db.Column(db.Integer, db.ForeignKey('vehicles.id'), db.ForeignKey('characters.id'), db.ForeignKey('planets.id'))
    fav_name = db.Column(db.String(250), ForeignKey('vehicles.name'), db.ForeignKey('characters.name'), db.ForeignKey('planets.name'))
    fav_Section = db.Column(db.String(250), db.ForeignKey('vehicles.user'), db.ForeignKey('characters.user'), db.ForeignKey('planets.user'))
