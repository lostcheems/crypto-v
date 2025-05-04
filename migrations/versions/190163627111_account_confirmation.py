"""账户确认

修订 ID: 190163627111
前一个修订: 456a945560f6
创建日期: 2013-12-29 02:58:45.577428

"""

# 修订标识符，由 Alembic 生成。
revision = '190163627111'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_column('users', 'confirmed')
    ### Alembic 命令结束 ###
