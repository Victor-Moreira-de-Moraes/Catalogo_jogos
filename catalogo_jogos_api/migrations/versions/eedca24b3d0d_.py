"""empty message

Revision ID: eedca24b3d0d
Revises: 0d0eda1007c6
Create Date: 2023-04-22 21:55:49.717631

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eedca24b3d0d'
down_revision = '0d0eda1007c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('titulo', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('descricao', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('data_lancamento', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('desenvolvedora', sa.String(length=100), nullable=False))
        batch_op.drop_column('nome')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', mysql.VARCHAR(length=50), nullable=False))
        batch_op.drop_column('desenvolvedora')
        batch_op.drop_column('data_lancamento')
        batch_op.drop_column('descricao')
        batch_op.drop_column('titulo')

    # ### end Alembic commands ###
