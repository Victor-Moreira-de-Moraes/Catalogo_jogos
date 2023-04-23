from flask_restful import Resource
from ..schemas import genero_schema
from flask import request, make_response, jsonify
from ..entidades import genero
from ..services import genero_service
from api import api

class GeneroList(Resource):
    def post(self):
        cs = genero_schema.GeneroSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            genero_novo = genero.Genero(
                nome=nome
            )
            resultado = genero_service.cadastrar_genero(genero_novo)
            return make_response(cs.jsonify(resultado), 201)

    def get(self):
        genero = genero_service.listar_genero()
        gs = genero_schema.GeneroSchema(many=True)
        return make_response(gs.jsonify(genero), 201)

class GeneroDetail(Resource):
    def get(self, id):
        genero = genero_service.listar_genero_id(id)

        if genero is None:
            return make_response(jsonify("Gênero não encontrado!!!"), 404)

        gs = genero_schema.GeneroSchema()
        return make_response(gs.jsonify(genero), 200)

    def put(self,id):
        genero_db = genero_service.listar_genero_id(id)

        if genero_db is None:
            return make_response(jsonify("Gênero não encontrado!!!"), 404)

        gs = genero_schema.GeneroSchema()
        validate = gs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            genero_novo = genero.Genero(nome=nome)
            resultado = genero_service.atualizar_genero(genero_db, genero_novo)
            return make_response(gs.jsonify(resultado), 201)

    def delete(self,id):
        genero = genero_service.listar_genero_id(id)

        if genero is None:
            return make_response(jsonify("Gênero não encontrado"), 404)

        genero_service.excluir_genero(genero)
        return make_response(jsonify("Gênero excluido com sucesso!!!"), 204)

api.add_resource(GeneroList,'/genero')
api.add_resource(GeneroDetail,'/genero/<int:id>')
