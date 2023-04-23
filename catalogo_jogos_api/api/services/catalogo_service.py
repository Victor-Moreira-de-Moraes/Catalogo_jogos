from api import db
from ..models import catalogo_model

def cadastrar_catalogo(catalogo):
    catalogo_db = catalogo_model.Catalogo(
        titulo=catalogo.titulo,
        descricao=catalogo.descricao,
        data_lancamento=catalogo.data_lancamento,
        desenvolvedora=catalogo.desenvolvedora,
        genero_id = catalogo.genero
    )
    db.session.add(catalogo_db)
    db.session.commit()
    return catalogo_db

def listar_catalogo():
    catalogo = catalogo_model.Catalogo.query.all()
    return catalogo

def listar_catalogo_id(id):
    catalogo = catalogo_model.Catalogo.query.filter_by(id=id).first()
    return catalogo

def atualizar_catalogo(catalogo, catalogo_novo):
    catalogo.titulo = catalogo_novo.titulo
    catalogo.descricao = catalogo_novo.descricao
    catalogo.data_lancamento = catalogo_novo.data_lancamento
    catalogo.desenvolvedora = catalogo_novo.desenvolvedora
    catalogo.genero_id = catalogo_novo.genero
    db.session.commit()
    return catalogo

def exclui_catalogo(catalogo):
    db.session.delete(catalogo)
    db.session.commit()
