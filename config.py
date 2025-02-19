import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:root@localhost/user-info'
    SQLALCHEMY_BINDS = {
        'user_data': 'mysql+pymysql://root:root@localhost/user-info',
        'algorithm_cases': 'mysql+pymysql://root:root@localhost/algorithm'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False