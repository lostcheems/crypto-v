from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional
from app.models import User

class LoginForm(FlaskForm):
    account = StringField('账号', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    account = StringField('账号', validators=[DataRequired()])
    group_id = IntegerField('群组号', validators=[Optional()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField(
        '确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('请使用不同的用户名。')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('请使用不同的邮箱地址。')

    def validate_account(self, account):
        user = User.query.filter_by(account=account.data).first()
        if user is not None:
            raise ValidationError('请使用不同的账号。')