"""create user integrations table

Revision ID: 0d9f889614e9
Revises: 394e9e4441d3
Create Date: 2021-12-19 17:58:40.786843

"""
from alembic import op
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '0d9f889614e9'
down_revision = '5c80e9e05547'
branch_labels = None
depends_on = None
table_name = 'user_integrations'


def upgrade():
    op.create_table(table_name,
                    Column('id', UUID(as_uuid=False), server_default=text('gen_random_uuid()'), primary_key=True),
                    Column('channel_id', UUID(as_uuid=False), ForeignKey('channels.id')),
                    Column('destination', String(255), nullable=False),
                    Column('name', String(255), nullable=False),  # user identifiable name
                    Column('created_at', TIMESTAMP, server_default=text('now()')),
                    )


def downgrade():
    op.drop_table(table_name)
