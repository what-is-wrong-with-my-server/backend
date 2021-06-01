"""empty message

Revision ID: 542345d1af6e
Revises: 53a4974865c1
Create Date: 2021-05-31 20:33:38.189710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542345d1af6e'
down_revision = '53a4974865c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('read_data', sa.Column('data', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('read_data', 'data')
    # ### end Alembic commands ###