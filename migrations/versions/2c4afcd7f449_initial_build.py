"""initial build

Revision ID: 2c4afcd7f449
Revises: 
Create Date: 2021-09-06 11:05:43.798008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c4afcd7f449'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_email'), 'admin', ['email'], unique=True)
    op.create_index(op.f('ix_admin_username'), 'admin', ['username'], unique=False)
    op.create_table('climb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climb_name', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=20), nullable=True),
    sa.Column('picture_path', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('getting_there', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_climb_climb_name'), 'climb', ['climb_name'], unique=False)
    op.create_index(op.f('ix_climb_description'), 'climb', ['description'], unique=False)
    op.create_index(op.f('ix_climb_getting_there'), 'climb', ['getting_there'], unique=False)
    op.create_index(op.f('ix_climb_location'), 'climb', ['location'], unique=False)
    op.create_index(op.f('ix_climb_picture_path'), 'climb', ['picture_path'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_climb_picture_path'), table_name='climb')
    op.drop_index(op.f('ix_climb_location'), table_name='climb')
    op.drop_index(op.f('ix_climb_getting_there'), table_name='climb')
    op.drop_index(op.f('ix_climb_description'), table_name='climb')
    op.drop_index(op.f('ix_climb_climb_name'), table_name='climb')
    op.drop_table('climb')
    op.drop_index(op.f('ix_admin_username'), table_name='admin')
    op.drop_index(op.f('ix_admin_email'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###