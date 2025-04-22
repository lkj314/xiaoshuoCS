from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os  # 新增导入

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key')  # 安全加固
# 修改为带默认值的环境变量获取方式
database_url = os.environ.get('DATABASE_URL', 'sqlite:///local.db')  # 本地开发默认用SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = database_url.replace("postgres://", "postgresql://", 1) if database_url else 'sqlite:///local.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# 导入路由和模型
from models import *
from routes import *

# 删除底部的启动代码
# if __name__ == '__main__':
#     app.run()