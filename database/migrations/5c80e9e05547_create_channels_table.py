"""create channels table

Revision ID: 5c80e9e05547
Revises: 
Create Date: 2021-12-18 00:24:52.926841

"""
from alembic import op
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '5c80e9e05547'
down_revision = None
branch_labels = None
depends_on = None
table_name = 'channels'


def upgrade():
    op.create_table(table_name,
                    Column('id', UUID(as_uuid=False), server_default=text('gen_random_uuid()'), primary_key=True),
                    Column('name', String(255), nullable=False),
                    Column('secret', String(255), nullable=False),
                    Column('created_at', TIMESTAMP, server_default=text('now()')),
                    )


def downgrade():
    op.drop_table(table_name)
