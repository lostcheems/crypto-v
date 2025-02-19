from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Group, Role, UserGroup
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse
from sqlalchemy import text

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(account=form.account.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('账号或密码无效')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='登录', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, account=form.account.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你，你现在是注册用户了！')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)

@app.route('/test_db')
def test_db():
    try:
        # 测试数据库连接
        db.session.execute(text('SELECT 1'))
        return render_template('test_db.html', message='数据库连接成功！')
    except Exception as e:
        return render_template('test_db.html', message=f'数据库连接失败：{e}')