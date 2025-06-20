"""rename address

Revision ID: 148fa9a0383a
Revises: 0c06f6d2adda
Create Date: 2025-06-12 19:52:59.313258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '148fa9a0383a'
down_revision = '0c06f6d2adda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###
