from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.models import db, Post

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    """首页

    Returns:
        _type_: _description_
    """
    posts  = Post.query.all()
    return render_template('blog/index.html', posts=posts)