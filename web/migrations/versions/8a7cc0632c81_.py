"""Added advert_for field for posts to simulate advertisements

Revision ID: 8a7cc0632c81
Revises: 21d3a64dad9a
Create Date: 2017-03-09 11:58:41.475333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a7cc0632c81'
down_revision = '21d3a64dad9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('advert_for_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'page', ['advert_for_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'advert_for_id')
    # ### end Alembic commands ###
