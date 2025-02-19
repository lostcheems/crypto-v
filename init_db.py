from app import app, db
from app.models import User, Role

def init_db():
    with app.app_context():
        db.create_all()

        # 获取系统管理员角色
        admin_role = Role.query.filter_by(name='系统管理员').first()
        if not admin_role:
            admin_role = Role(name='系统管理员', description='系统管理员角色')
            db.session.add(admin_role)
            db.session.commit()

        # 创建系统管理员用户
        admin_user = User(username='admin', account=100000, role_id=admin_role.id)
        admin_user.set_password('admin')
        db.session.add(admin_user)
        db.session.commit()

        print('数据库初始化完成，系统管理员用户已创建。')

if __name__ == '__main__':
    init_db()