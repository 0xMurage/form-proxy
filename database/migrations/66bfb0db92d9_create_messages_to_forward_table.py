"""create messages to forward table

Revision ID: 66bfb0db92d9
Revises: c0ba5ceac00d
Create Date: 2021-12-19 19:31:12.593765

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '66bfb0db92d9'
down_revision = 'c0ba5ceac00d'
branch_labels = None
depends_on = None
table_name = 'messages_to_forward'


def upgrade():
    op.create_table(table_name,
                    Column('id', UUID(as_uuid=False), server_default=text('gen_random_uuid()'), primary_key=True),
                    Column('integration_id', UUID(as_uuid=False), ForeignKey('user_integrations.id'), nullable=False),
                    Column('message', Text),
                    Column('sent', Boolean, default=False),
                    Column('created_at', TIMESTAMP, server_default=text('now()')),
                    Column('updated_at', TIMESTAMP, server_default=text('now()')),
                    )


def downgrade():
    op.drop_table(table_name)
