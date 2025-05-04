"""登录支持

修订 ID: 456a945560f6
前一个修订: 38c4e85512a9
创建日期: 2013-12-29 00:18:35.795259

"""

# 修订标识符，由 Alembic 生成。
revision = '456a945560f6'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_index('ix_users_email', 'users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    ### Alembic 命令结束 ###
