Crypto_VIZ
======

此项目是一个基于 Flask 框架的 Web 应用程序，包含用户认证、博客文章、评论、密码算法可视化、关注系统等功能。

### 项目目录结构
flasky/ │ ├── app/ # 应用程序模块 
        │ ├── templates/ # HTML 模板文件 
        │ ├── static/ # 静态文件（CSS、JS、图片等） 
        │ ├── models.py # 数据库模型定义 
        │ ├── views.py # 视图函数 
        │ └── init.py # 应用初始化 
        │ ├── migrations/ # 数据库迁移脚本 
        │ ├── tests/ # 单元测试 
        │ ├── test_api.py # API 测试 
        │ ├── test_client.py # 客户端测试 
        │ └── test_user_model.py # 用户模型测试 
        │ ├── config.py # 配置文件 
        ├── flasky.py # 应用程序入口 
        └── requirements.txt # 项目依赖

### 功能介绍

1. **用户认证**：支持用户注册、登录、登出、邮箱验证、密码重置等功能。
2. **文章管理**：用户可以发布、编辑和删除文章。
3. **关注系统**：用户可以关注其他用户，并查看关注者的文章。
4. **管理员功能**：管理员可以管理用户和评论。

### 如何运行项目
初始化数据库：flask db init
生成迁移脚本：flask db migrate -m "message"
更新数据库：flask db upgrade

设置环境变量：$env:FLASK_APP="crypto_viz.py"
运行项目：flask run