import re
import threading
import time
import unittest
from selenium import webdriver
from app import create_app, db, fake
from app.models import Role, User, Post


class SeleniumTestCase(unittest.TestCase):
    client = None
    
    @classmethod
    def setUpClass(cls):
        # 启动 Chrome 浏览器
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        try:
            cls.client = webdriver.Chrome(chrome_options=options)
        except:
            pass

        # 如果浏览器无法启动，则跳过这些测试
        if cls.client:
            # 创建应用程序
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # 禁用日志记录以保持 unittest 输出干净
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")

            # 创建数据库并填充一些虚拟数据
            db.create_all()
            Role.insert_roles()
            fake.users(10)
            fake.posts(10)

            # 添加管理员用户
            admin_role = Role.query.filter_by(name='Administrator').first()
            admin = User(email='john@example.com',
                         username='john', password='cat',
                         role=admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            # 在一个线程中启动 Flask 服务器
            cls.server_thread = threading.Thread(target=cls.app.run,
                                                 kwargs={'debug': False})
            cls.server_thread.start()

            # 给服务器一秒钟以确保其启动
            time.sleep(1) 

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # 停止 Flask 服务器和浏览器
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.quit()
            cls.server_thread.join()

            # 销毁数据库
            db.drop_all()
            db.session.remove()

            # 移除应用程序上下文
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web 浏览器不可用')

    def tearDown(self):
        pass
    
    def test_admin_home_page(self):
        # 访问主页
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('你好，\s+陌生人!',
                                  self.client.page_source))

        # 访问登录页面
        self.client.find_element_by_link_text('登录').click()
        self.assertIn('<h1>登录</h1>', self.client.page_source)

        # 登录
        self.client.find_element_by_name('email').\
            send_keys('john@example.com')
        self.client.find_element_by_name('password').send_keys('cat')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('你好，\s+john!', self.client.page_source))

        # 访问用户的个人资料页面
        self.client.find_element_by_link_text('个人资料').click()
        self.assertIn('<h1>john</h1>', self.client.page_source)
