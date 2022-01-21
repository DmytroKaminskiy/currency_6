"""Added required tables

Revision ID: 02669332fc73
Revises: 
Create Date: 2022-01-20 19:03:49.235752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02669332fc73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zoom_webhook_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=100), nullable=True),
    sa.Column('event_ts', sa.BigInteger(), nullable=True),
    sa.Column('payload', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zoom_webhook_events_event'), 'zoom_webhook_events', ['event'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_zoom_webhook_events_event'), table_name='zoom_webhook_events')
    op.drop_table('zoom_webhook_events')
    # ### end Alembic commands ###