from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///novels.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# 导入路由和模型
from models import *
from routes import *

if __name__ == '__main__':
    app.run()