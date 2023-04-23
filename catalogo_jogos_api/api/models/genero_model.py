from api import db

class Genero(db.Model):
    __tablename__ = 'genero'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
