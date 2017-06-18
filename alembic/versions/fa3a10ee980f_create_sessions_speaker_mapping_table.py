"""create sessions speaker mapping table

Revision ID: fa3a10ee980f
Revises: 456a4424a15c
Create Date: 2017-06-18 15:08:18.203585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3a10ee980f'
down_revision = '456a4424a15c'
branch_labels = None
depends_on = None

meta = sa.MetaData()
def upgrade():
    op.create_table(
        'session_speakers', meta,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('fk_session', sa.Integer,sa.ForeignKey('sessions.id'), nullable=False),
        sa.Column('fk_speaker', sa.Integer,sa.ForeignKey('speakers.id'),nullable=False)
    )


def downgrade():
    op.drop_table('session_speakers')
