"""文章模型

修订 ID: 1b966e7f4b9e
前一个修订: 198b0eebcf9
创建日期: 2013-12-31 00:00:14.700591

"""

# 修订标识符，由 Alembic 生成。
revision = '1b966e7f4b9e'
down_revision = '198b0eebcf9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_index('ix_posts_timestamp', 'posts')
    op.drop_table('posts')
    ### Alembic 命令结束 ###
