"""评论表

修订 ID: 51f5ccfba190
前一个修订: 2356a38169ea
创建日期: 2014-01-01 12:08:43.287523

"""

# 修订标识符，由 Alembic 生成。
revision = '51f5ccfba190'
down_revision = '2356a38169ea'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    pass   
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_index('ix_comments_timestamp', 'comments')
    op.drop_table('comments')
    ### Alembic 命令结束 ###
