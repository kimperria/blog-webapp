
from flask import flash, render_template, redirect,url_for
from app.main import main
from app.models import Blog
from app.request import get_random_qoutes
from app.main.forms import BlogForm
from app import db



@main.route('/')
@main.route('/index')
def index():
    '''
    View function that sets index page
    '''
    title = 'Home'
    random_quote = get_random_qoutes()

    return render_template('index.html', title=title, quotes=random_quote)



@main.route('/createblog', methods=['GET','POST'])
def createblog():
    '''
    View function that sets blog page
    '''
    title = 'Create blog'
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(blog_post=form.blog_post.data, blog_title=form.blog_title.data)
        db.session.add(blog)
        db.session.commit()
        flash('Blog has been created')
        return redirect(url_for('main.index'))

    return render_template('blog.html', title=title, form=form)


    