"""create speakers table

Revision ID: 437fd24e4487
Revises: 
Create Date: 2017-06-17 21:07:17.737356

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '437fd24e4487'
down_revision = None
branch_labels = None
depends_on = None

meta = sa.MetaData()

speakers = sa.Table


def upgrade():
    op.create_table(
        'speakers', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('dp_url', sa.String(250)),
        sa.Column('profile_url', sa.String(250))
    )


def downgrade():
    op.drop_table('speakers')
