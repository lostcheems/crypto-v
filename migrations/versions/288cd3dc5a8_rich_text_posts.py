"""富文本文章

修订 ID: 288cd3dc5a8
前一个修订: 1b966e7f4b9e
创建日期: 2013-12-31 03:25:13.286503

"""

# 修订标识符，由 Alembic 生成。
revision = '288cd3dc5a8'
down_revision = '1b966e7f4b9e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_column('posts', 'body_html')
    ### Alembic 命令结束 ###
