from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class NovelForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('简介')

class CommentForm(FlaskForm):
    content = TextAreaField('评论内容', validators=[DataRequired()])