from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# 这是 Alembic 配置对象，用于访问正在使用的 .ini 文件中的值。
config = context.config

# 解释配置文件以进行 Python 日志记录。
# 这行代码基本上设置了日志记录器。
fileConfig(config.config_file_name)

# 在此处添加模型的 MetaData 对象
# 以支持 'autogenerate' 功能
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from flask import current_app
config.set_main_option('sqlalchemy.url', current_app.config.get('SQLALCHEMY_DATABASE_URI'))
target_metadata = current_app.extensions['migrate'].db.metadata

# 其他由 env.py 的需求定义的配置值
# 可以通过以下方式获取：
# my_important_option = config.get_main_option("my_important_option")
# ... 等等。

def run_migrations_offline():
    """以 '离线' 模式运行迁移。

    这会使用 URL 配置上下文，而不是引擎，
    尽管这里也可以接受引擎。通过跳过引擎创建，
    我们甚至不需要可用的 DBAPI。

    在此处调用 context.execute() 会将给定的字符串输出到脚本。

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """以 '在线' 模式运行迁移。

    在这种情况下，我们需要创建一个引擎
    并将连接与上下文关联。

    """
    engine = engine_from_config(
                config.get_section(config.config_ini_section),
                prefix='sqlalchemy.',
                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
                connection=connection,
                target_metadata=target_metadata
                )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

