"""adding-restaurant-relationship

Revision ID: dec3cc1d65f2
Revises: e549a5e99a06
Create Date: 2023-11-22 05:31:00.607257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dec3cc1d65f2'
down_revision: Union[str, None] = 'e549a5e99a06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###