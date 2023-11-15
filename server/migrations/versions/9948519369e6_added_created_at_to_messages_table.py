"""added created_at to messages table

Revision ID: 9948519369e6
Revises: e27c13271409
Create Date: 2023-11-15 14:22:59.389271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9948519369e6'
down_revision = 'e27c13271409'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'created_at')
    # ### end Alembic commands ###
