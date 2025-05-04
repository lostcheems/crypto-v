import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

import sys
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post

# 创建 Flask 应用程序实例
app = create_app('development')  # 使用开发配置
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    # 为 Flask shell 提供上下文
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
              help='在代码覆盖率下运行测试。')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
    """运行单元测试。"""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('覆盖率摘要：')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML 版本：file://%s/index.html' % covdir)
        COV.erase()


@app.cli.command()
@click.option('--length', default=25,
              help='性能分析报告中包含的函数数量。')
@click.option('--profile-dir', default=None,
              help='保存性能分析数据文件的目录。')
def profile(length, profile_dir):
    """在代码性能分析器下启动应用程序。"""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


@app.cli.command()
def deploy():
    """运行部署任务。"""
    # 将数据库迁移到最新修订版本
    upgrade()

    # 创建或更新用户角色
    Role.insert_roles()

    # 确保所有用户都关注自己
    User.add_self_follows()
