"""Added quantity_value and quantity_unit column

Revision ID: 200b1c10599b
Revises: 
Create Date: 2025-12-07 19:23:10.478028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '200b1c10599b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('kitchen' , sa.Column())
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
