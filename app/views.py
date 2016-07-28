from flask import render_template, url_for, request, make_response, redirect
from .forms import loginform, pushpostform
from app import app
from .model import User, Post


@app.route('/')
@app.route('/index')
def index():
    title = 'shijun'
    return render_template('index.html', title=title)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = loginform()
    username = None
    password = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return redirect(url_for('index'))
    return render_template('login.html', form=form, username=username, password=password)


@app.route('/pushpost', methods=["POST", "GET"])
def pushpost():
    form = pushpostform()
    # post = request.form.post.data
    if form.validate_on_submit():
        post = form.post.value
        data = form.date.data
        redirect(url_for('index'))
    return render_template('post.html', form=form, post=post)
