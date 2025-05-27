"""rename created_at to create_at

Revision ID: 36bbbb6a3338
Revises: 2dd5d8573463
Create Date: 2025-05-26 11:47:24.926057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36bbbb6a3338'
down_revision: Union[str, None] = '2dd5d8573463'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('users', 'created_at')
    op.drop_column('posts', 'created_at')

    # Add correct columns
    op.add_column('users', sa.Column('create_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('posts', sa.Column('create_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('users', 'create_at')
    op.drop_column('posts', 'create_at')

    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))

    pass
