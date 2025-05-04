"""用户角色

修订 ID: 56ed7d33de8d
前一个修订: 190163627111
创建日期: 2013-12-29 22:19:54.212604

"""

# 修订标识符，由 Alembic 生成。
revision = '56ed7d33de8d'
down_revision = '190163627111'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_index('ix_roles_default', 'roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### Alembic 命令结束 ###
