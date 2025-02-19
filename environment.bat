@echo off
REM 创建项目目录结构

mkdir app
mkdir app\templates
mkdir app\static
mkdir app\static\css
mkdir app\static\js
mkdir migrations
python -m venv venv

REM 创建文件
type nul > app\__init__.py
type nul > app\routes.py
type nul > app\models.py
type nul > app\forms.py
type nul > app\templates\base.html
type nul > app\templates\index.html
type nul > app\templates\login.html
type nul > app\templates\register.html
type nul > app\templates\user_management.html
type nul > app\templates\group_management.html
type nul > app\templates\algorithm_display.html
type nul > app\templates\password_evaluation.html
type nul > app\static\css\style.css
type nul > app\static\js\script.js
type nul > config.py
type nul > requirements.txt


echo 项目目录结构已创建。