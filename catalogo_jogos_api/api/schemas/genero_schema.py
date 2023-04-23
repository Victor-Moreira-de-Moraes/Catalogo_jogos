from api import ma
from ..models import genero_model
from marshmallow import fields
from ..schemas import catalogo_schema

class GeneroSchema(ma.SQLAlchemyAutoSchema):
    catalogos = ma.Nested(catalogo_schema.CatalogoSchema, many=True, only=('titulo', 'descricao', 'data_lancamento', 'desenvolvedora'))

    class Meta:
        model = genero_model.Genero
        load_instance = True

        nome = fields.String(required=True)
