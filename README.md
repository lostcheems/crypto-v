# crypto-v

## 项目概述
`crypto-v` 是一个基于 Flask 的网络应用，旨在提供一个用户友好的界面，用于加密货币相关的功能。该项目结构清晰，便于导航和维护。

## 目录结构
```
crypto-v
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── user_management.html
│   │   ├── group_management.html
│   │   ├── algorithm_display.html
│   │   └── password_evaluation.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── script.js
├── migrations
├── venv
├── config.py
├── requirements.txt
└── README.md
```
## 目录功能介绍
- `app/__init__.py`: 初始化 Flask 应用及其扩展。
- `app/routes.py`: 定义应用的路由和视图函数。
- `app/models.py`: 定义数据库模型。
- `app/forms.py`: 定义表单类。
- `app/templates/`: 存放 HTML 模板文件。
  - `base.html`: 基础模板，其他模板继承自此模板。
  - `index.html`: 首页模板。
  - `login.html`: 登录页面模板。
  - `register.html`: 注册页面模板。
  - `user_management.html`: 用户管理页面模板。
  - `group_management.html`: 群组管理页面模板。
  - `algorithm_display.html`: 算法展示页面模板。
  - `password_evaluation.html`: 密码评估页面模板。
- `app/static/`: 存放静态文件（CSS、JavaScript 等）。
  - `css/style.css`: CSS 样式文件。
  - `js/script.js`: JavaScript 脚本文件。
- `migrations/`: 存放数据库迁移文件。
- `venv/`: 虚拟环境目录。
- `config.py`: 配置文件。
- `requirements.txt`: 列出项目依赖的 Python 包。
- `README.md`: 项目说明文件。

## 使用
1. 设置 Flask 的环境变量：
- 在 Windows 上：
  ```
  set FLASK_APP=app
  ```
- 在 macOS/Linux 上：
  ```
  export FLASK_APP=app
  ```
2. 运行应用：
   ```
   flask run
   ```
3. 打开浏览器并访问 `http://127.0.0.1:5000` 以访问应用。

## 贡献
欢迎贡献！请通过提交 issue 或 pull request 来提出任何增强功能或错误修复。

## 许可证
该项目使用 MIT 许可证。详情请参阅 LICENSE 文件。