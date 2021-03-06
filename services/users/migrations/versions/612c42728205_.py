"""empty message

Revision ID: 612c42728205
Revises: 
Create Date: 2020-12-23 01:03:40.440919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '612c42728205'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
