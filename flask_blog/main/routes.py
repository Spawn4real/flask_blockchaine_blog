from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home(name=None):
    return render_template('home.html', name=name)


@main.route("/blog")
def blog(name=None):
    return render_template('blog-grid.html', name=name)


@main.route("/signup")
def signup(name=None):
    return render_template('signup.html', name=name)


@main.route("/404")
def error(name=None):
    return render_template('404.html', name=name)

