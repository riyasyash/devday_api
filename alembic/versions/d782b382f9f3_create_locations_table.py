"""create locations table

Revision ID: d782b382f9f3
Revises: 437fd24e4487
Create Date: 2017-06-18 13:04:38.208433

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd782b382f9f3'
down_revision = '437fd24e4487'
branch_labels = None
depends_on = None

meta = sa.MetaData()


def upgrade():
    op.create_table(
        'locations', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('place', sa.String(50), nullable=False),
        sa.Column('location_url', sa.String(250))
    )


def downgrade():
    op.drop_table('locations')
