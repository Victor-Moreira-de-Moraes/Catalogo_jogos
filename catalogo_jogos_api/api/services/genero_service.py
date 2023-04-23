from api import db
from ..models import genero_model

def cadastrar_genero(genero):
    genero_db = genero_model.Genero(
        nome = genero.nome
    )

    db.session.add(genero_db)
    db.session.commit()
    return genero_db

def listar_genero():
    genero = genero_model.Genero.query.all()
    return genero

def listar_genero_id(id):
    genero = genero_model.Genero.query.filter_by(id=id).first()
    return genero


def atualizar_genero(genero, genero_novo):
    genero.nome = genero_novo.nome
    db.session.commit()
    return genero

def excluir_genero(genero):
    db.session.delete(genero)
    db.session.commit()
