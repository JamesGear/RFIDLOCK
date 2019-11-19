"""empty message

Revision ID: caac81fbb1f3
Revises: 0b8851fc67c9
Create Date: 2019-11-12 10:26:33.372597

"""

# revision identifiers, used by Alembic.
revision = 'caac81fbb1f3'
down_revision = '0b8851fc67c9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Firma', sa.Column('parent_id_group', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Firma', 'Group', ['parent_id_group'], ['id'])
    op.drop_constraint('Group_parent_id_firma_fkey', 'Group', type_='foreignkey')
    op.drop_column('Group', 'parent_id_firma')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Group', sa.Column('parent_id_firma', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Group_parent_id_firma_fkey', 'Group', 'Firma', ['parent_id_firma'], ['id'])
    op.drop_constraint(None, 'Firma', type_='foreignkey')
    op.drop_column('Firma', 'parent_id_group')
    # ### end Alembic commands ###
