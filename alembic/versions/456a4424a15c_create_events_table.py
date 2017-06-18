"""create events table

Revision ID: 456a4424a15c
Revises: 1b7e2ca22957
Create Date: 2017-06-18 14:00:25.778893

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '456a4424a15c'
down_revision = '1b7e2ca22957'
branch_labels = None
depends_on = None

meta = sa.MetaData()


def upgrade():
    op.create_table(
        'events', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(500)),
        sa.Column('meetup_link', sa.String(250)),
        sa.Column('fk_location_id', sa.Integer,sa.ForeignKey("locations.id"),nullable=False)

    )


def downgrade():
    op.drop_table('events')
