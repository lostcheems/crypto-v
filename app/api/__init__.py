from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users,  errors, algorithm  # 确保导入 algorithm
