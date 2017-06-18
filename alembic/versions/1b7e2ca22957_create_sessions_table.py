"""create sessions table

Revision ID: 1b7e2ca22957
Revises: d782b382f9f3
Create Date: 2017-06-18 13:47:15.439897

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1b7e2ca22957'
down_revision = 'd782b382f9f3'
branch_labels = None
depends_on = None

meta = sa.MetaData()


def upgrade():
    op.create_table(
        'sessions', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('topic', sa.String(100), nullable=False),
        sa.Column('description', sa.String(250))
    )


def downgrade():
    op.drop_table('sessions')
