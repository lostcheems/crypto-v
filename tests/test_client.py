import re
import unittest
from app import create_app, db
from app.models import User, Role

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        # 设置测试环境
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        # 清理测试环境
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        # 测试主页
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('陌生人' in response.get_data(as_text=True))

    def test_register_and_login(self):
        # 注册一个新账户
        response = self.client.post('/auth/register', data={
            'email': 'john@example.com',
            'username': 'john',
            'password': 'cat',
            'password2': 'cat'
        })
        self.assertEqual(response.status_code, 302)

        # 使用新账户登录
        response = self.client.post('/auth/login', data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(re.search('你好，\s+john!',
                                  response.get_data(as_text=True)))
        self.assertTrue(
            '您尚未确认您的账户' in response.get_data(as_text=True))

        # 发送确认令牌
        user = User.query.filter_by(email='john@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get('/auth/confirm/{}'.format(token),
                                   follow_redirects=True)
        user.confirm(token)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            '您已确认您的账户' in response.get_data(as_text=True))

        # 注销
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('您已注销' in response.get_data(as_text=True))
