"""empty message

Revision ID: 1886851952d4
Revises: 9393ef2644c5
Create Date: 2021-09-19 22:47:39.078158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1886851952d4'
down_revision = '9393ef2644c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'favorites', 'user', ['id_user'], ['id'])
    # ### end Alembic commands ###
