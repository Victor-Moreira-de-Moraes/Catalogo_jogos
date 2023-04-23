from flask_restful import Resource
from ..schemas import catalogo_schema
from flask import request, make_response, jsonify
from ..entidades import catalogo
from ..services import catalogo_service
from api import api

class CatalogoList(Resource):
    def post(self):
        cs = catalogo_schema.CatalogoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_lancamento = request.json["data_lancamento"]
            desenvolvedora = request.json["desenvolvedora"]
            genero = request.json["genero_id"]
            catalogo_novo = catalogo.Catalogo(titulo=titulo, descricao=descricao, data_lancamento=data_lancamento, desenvolvedora=desenvolvedora, genero=genero)
            resultado = catalogo_service.cadastrar_catalogo(catalogo_novo)
            return make_response(cs.jsonify(resultado), 201)

class CatalogoList(Resource):
    def get(self):
        catalogo = catalogo_service.listar_catalogo()
        cs = catalogo_schema.CatalogoSchema(many=True)
        return make_response(cs.jsonify(catalogo), 201)

class CatalogoDetail(Resource):
    def get(self, id):
        catalogo = catalogo_service.listar_catalogo_id(id)

        if catalogo is None:
            return make_response(jsonify("Jogo não encontrado!!!"), 404)

        cs = catalogo_schema.CatalogoSchema()
        return make_response(cs.jsonify(catalogo), 200)

    def put(self,id):
        catalogo_db = catalogo_service.listar_catalogo_id(id)

        if catalogo_db is None:
            return make_response(jsonify("Jogo não encontrado!!!"), 404)

        cs = catalogo_schema.CatalogoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_lancamento = request.json["data_lancamento"]
            desenvolvedora = request.json["desenvolvedora"]
            genero = request.json["genero_id"]
            catalogo_novo = catalogo.Catalogo(titulo=titulo, descricao=descricao, data_lancamento=data_lancamento, desenvolvedora=desenvolvedora, genero=genero)
            resultado = catalogo_service.atualizar_catalogo(catalogo_db, catalogo_novo)
            return make_response(cs.jsonify(resultado), 201)

    def delete(self, id):
        catalogo = catalogo_service.listar_catalogo_id(id)

        if catalogo is None:
            return make_response(jsonify("Jogo não encontrado!!!"), 404)

        catalogo_service.exclui_catalogo(catalogo)
        return make_response(jsonify(""), 204)

api.add_resource(CatalogoList,'/catalogo')
api.add_resource(CatalogoDetail, '/catalogo/<int:id>')
