"""social account added
Revision ID: 2418b094fffd
Revises: 93a756470bc9
Create Date: 2021-11-29 20:04:57.900960
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2418b094fffd'
down_revision = '93a756470bc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social_accounts',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('social_id', sa.String(length=255), nullable=False),
    sa.Column('social_name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['content.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('social_id', 'social_name', name='social_uc'),
    schema='content'
    )
    op.create_unique_constraint('auth_history_uc', 'auth_history', ['id'], schema='content')
    op.create_unique_constraint('roles_uc', 'roles', ['id'], schema='content')
    op.create_unique_constraint('users_uc', 'users', ['id'], schema='content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_uc', 'users', schema='content', type_='unique')
    op.drop_constraint('roles_uc', 'roles', schema='content', type_='unique')
    op.drop_constraint('auth_history_uc', 'auth_history', schema='content', type_='unique')
    op.drop_table('social_accounts', schema='content')
    # ### end Alembic commands ###