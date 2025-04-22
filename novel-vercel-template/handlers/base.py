# ... existing code ...
# 添加小说相关路由
@app.route('/create-novel', methods=['GET','POST'])
@login_required
def create_novel():
    form = NovelForm()
    if form.validate_on_submit():
        new_novel = Novel(title=form.title.data, 
                        description=form.description.data,
                        author=current_user)
        db.session.add(new_novel)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_novel.html', form=form)