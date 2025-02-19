from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bcrypt = Bcrypt(app)
bootstrap = Bootstrap4(app)  # 初始化 Flask-Bootstrap

from app import routes, models

if __name__ == '__main__':
    app.run(debug=True)