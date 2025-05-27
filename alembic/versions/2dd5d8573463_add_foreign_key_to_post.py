"""add foreign key to post

Revision ID: 2dd5d8573463
Revises: 16f14236d1e7
Create Date: 2025-05-26 11:18:57.182673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dd5d8573463'
down_revision: Union[str, None] = '16f14236d1e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        'posts_users_fk',  # name of the foreign key constraint
        'posts',          # source table
        'users',          # referent table
        ['owner_id'],     # source column
        ['id']            # referent column
    )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
