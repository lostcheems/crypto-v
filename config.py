import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = None  # 禁用邮件服务器
    MAIL_PORT = None  # 禁用邮件端口
    MAIL_USE_TLS = False  # 禁用 TLS
    MAIL_USERNAME = None  # 禁用邮件用户名
    MAIL_PASSWORD = None  # 禁用邮件密码
    FLASKY_MAIL_SUBJECT_PREFIX = ''  # 禁用邮件主题前缀
    FLASKY_MAIL_SENDER = ''  # 禁用邮件发送者
    FLASKY_ADMIN = None  # 禁用管理员邮箱
    SSL_REDIRECT = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 20  # 每页文章数
    FLASKY_FOLLOWERS_PER_PAGE = 50  # 每页关注者数
    FLASKY_COMMENTS_PER_PAGE = 30  # 每页评论数
    FLASKY_SLOW_DB_QUERY_TIME = 0.5  # 慢查询时间阈值（秒）

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True  # 启用调试模式
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True  # 启用测试模式
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
    WTF_CSRF_ENABLED = False  # 禁用 CSRF 保护


class ProductionConfig(Config):
    SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost:5000')  # 默认值为 localhost:5000

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # 将错误通过邮件发送给管理员
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' 应用错误',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # 处理反向代理服务器头部
        try:
            from werkzeug.middleware.proxy_fix import ProxyFix
        except ImportError:
            from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # 将日志输出到标准错误
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # 将日志输出到标准错误
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # 将日志输出到系统日志
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.INFO)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,  # 开发配置
    'testing': TestingConfig,  # 测试配置
    'production': ProductionConfig,  # 生产配置
    'heroku': HerokuConfig,  # Heroku 配置
    'docker': DockerConfig,  # Docker 配置
    'unix': UnixConfig,  # Unix 配置

    'default': DevelopmentConfig  # 默认配置
}
