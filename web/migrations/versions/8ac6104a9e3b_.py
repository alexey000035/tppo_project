"""empty message

Revision ID: 8ac6104a9e3b
Revises: 8a7cc0632c81
Create Date: 2018-12-12 12:49:24.797274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ac6104a9e3b'
down_revision = '8a7cc0632c81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('is_danger', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'is_danger')
    # ### end Alembic commands ###
