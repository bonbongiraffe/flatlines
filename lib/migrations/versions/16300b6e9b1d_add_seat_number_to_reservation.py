"""add seat number to reservation

Revision ID: 16300b6e9b1d
Revises: 62f03ab23517
Create Date: 2023-07-18 17:15:08.068548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16300b6e9b1d'
down_revision = '62f03ab23517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('seat_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'seat_number')
    # ### end Alembic commands ###
