from app import create_app, db
from app.models import Role, User, Permission

app = create_app('default')
app.app_context().push()

# 初始化角色和权限
Role.insert_roles()
db.session.commit()
print("角色和权限已重新初始化。")

# 为指定用户赋予管理员权限
username = 'lostcheems'  # 替换为需要赋予管理员权限的用户名
user = User.query.filter_by(username=username).first()

if user:
    admin_role = Role.query.filter_by(name='Administrator').first()
    if admin_role:
        user.role = admin_role
        db.session.add(user)
        db.session.commit()
        print(f"用户 {user.username} 已赋予管理员权限。")
    else:
        print("管理员角色不存在，请检查角色初始化。")
else:
    print(f"用户 {username} 不存在。")

# 检查用户和角色
users = User.query.all()
for user in users:
    print(f"用户名: {user.username}, 角色: {user.role.name if user.role else '无角色'}")