"""Database init

Revision ID: a0e2ff66ecc2
Revises: 
Create Date: 2023-05-12 19:50:28.292894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0e2ff66ecc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('coords', sa.VARCHAR(length=21), nullable=False),
    sa.Column('closed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('museums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=40), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('coords', sa.VARCHAR(length=21), nullable=False),
    sa.Column('website', sa.VARCHAR(length=40), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('showrooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=40), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('coords', sa.VARCHAR(length=21), nullable=False),
    sa.Column('website', sa.VARCHAR(length=40), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=12), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wifi_zones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wifi_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('coords', sa.VARCHAR(length=21), nullable=False),
    sa.Column('coverage', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('universities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('metro', sa.Integer(), nullable=False),
    sa.Column('web_site', sa.VARCHAR(length=40), nullable=False),
    sa.Column('coords', sa.VARCHAR(length=21), nullable=False),
    sa.ForeignKeyConstraint(['metro'], ['metros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('universities')
    op.drop_table('wifi_zones')
    op.drop_table('showrooms')
    op.drop_table('museums')
    op.drop_table('metros')
    # ### end Alembic commands ###
