"""create trusted domains table

Revision ID: c0ba5ceac00d
Revises: 0d9f889614e9
Create Date: 2021-12-19 18:19:23.527875

"""
from alembic import op
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'c0ba5ceac00d'
down_revision = '0d9f889614e9'
branch_labels = None
depends_on = None
table_name = 'trusted_domains'


def upgrade():
    op.create_table(table_name,
                    Column('integration_id', UUID(as_uuid=False), ForeignKey('user_integrations.id'), nullable=False),
                    Column('domain', String(255), nullable=False),
                    Column('allowed', Boolean, default=True, nullable=False),
                    Column('created_at', TIMESTAMP, nullable=False, server_default=text('now()')),
                    UniqueConstraint('integration_id', 'domain', name='idm')
                    )


def downgrade():
    op.drop_table(table_name)
