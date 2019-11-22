"""empty message

Revision ID: ff33413a8d55
Revises: 971101b4e78e
Create Date: 2019-11-22 17:31:07.287670

"""

# revision identifiers, used by Alembic.
revision = 'ff33413a8d55'
down_revision = '971101b4e78e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cas_od_do', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'User', 'Cas', ['id_cas'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='foreignkey')
    op.drop_table('Cas')
    # ### end Alembic commands ###
