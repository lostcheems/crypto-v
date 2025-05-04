"""头像哈希缓存

修订 ID: 198b0eebcf9
前一个修订: d66f086b258
创建日期: 2014-02-04 09:10:02.245503

"""

# 修订标识符，由 Alembic 生成。
revision = '198b0eebcf9'
down_revision = 'd66f086b258'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_column('users', 'avatar_hash')
    ### Alembic 命令结束 ###
