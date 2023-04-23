from datetime import datetime
from api import db

class Catalogo(db.Model):
    __tablename__ = 'catalogo'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text())
    data_lancamento = db.Column(db.DateTime, default=datetime.utcnow)
    desenvolvedora = db.Column(db.String(100), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey("genero.id"))
    genero = db.relationship("Genero", backref=db.backref("catalogos"), lazy="raise")
