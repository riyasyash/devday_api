"""create event session mapping table

Revision ID: 217d70f39b8e
Revises: fa3a10ee980f
Create Date: 2017-06-18 15:18:48.949210

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = '217d70f39b8e'
down_revision = 'fa3a10ee980f'
branch_labels = None
depends_on = None

meta = sa.MetaData()


def upgrade():
    op.create_table(
        'event_session_speakers', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('fk_session_speaker', sa.Integer, sa.ForeignKey('session_speakers.id'), nullable=False),
        sa.Column('fk_event', sa.Integer, sa.ForeignKey('events.id'), nullable=False),
        sa.Column('date', sa.Date),
        sa.Column('start_time', sa.String(10)),
        sa.Column('end_time', sa.String(10))
    )


def downgrade():
    op.drop_table('event_session_speakers')
