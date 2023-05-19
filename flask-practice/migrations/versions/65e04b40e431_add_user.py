"""add user

Revision ID: 65e04b40e431
Revises: 
Create Date: 2023-05-19 08:37:34.355262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65e04b40e431'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_model')
    # ### end Alembic commands ###
