from flask import jsonify
from app.exceptions import ValidationError
from . import api


def bad_request(message):
    response = jsonify({'错误': '错误的请求', '消息': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'错误': '未授权', '消息': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'错误': '禁止访问', '消息': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
