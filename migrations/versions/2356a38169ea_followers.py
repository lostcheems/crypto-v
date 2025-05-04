"""关注者关系表

修订 ID: 2356a38169ea
前一个修订: 288cd3dc5a8
创建日期: 2013-12-31 16:10:34.500006

"""

# 修订标识符，由 Alembic 生成。
revision = '2356a38169ea'
down_revision = '288cd3dc5a8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    ### Alembic 命令结束 ###


def downgrade():
    ### Alembic 自动生成的命令 - 请根据需要调整！ ###
    op.drop_table('follows')
    ### Alembic 命令结束 ###
