# ... existing code ...
# 在原有模型基础上添加小说业务模型
class Novel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chapters = db.relationship('Chapter', backref='novel', lazy=True)

# 保留原模板的用户认证系统
class User(UserMixin, db.Model):
    # ... existing code ...
    novels = db.relationship('Novel', backref='author', lazy=True)  # 新增关联