from api import ma
from ..models import catalogo_model
from marshmallow import fields

class CatalogoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = catalogo_model.Catalogo
        load_instance = True
        include_fk = True

        titulo = fields.String(required=True)
        data_lancamento = fields.DateTime(required=True)
        desenvolvedora = fields.String(required=True)
        genero_id = fields.Integer(required=True)
