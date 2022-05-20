from flask import Blueprint, flash, g,redirect, render_template, request, session, url_for
from flaskr.models import db, User, Post
from werkzeug.security import check_password_hash, generate_password_hash
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """注册用户

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        
        if not username:
            error = "username is required."
        elif not password:
            error = "password is required."
        
        if error is None:
            user = User.query.filter_by(username=username).first()
            print(user)
            if user:
                error = f'用户名:{username}已注册.'
            else:
                user = User(username=username, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')
                

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """登录

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            error = 'Incorrect username or password.'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    """登出

    Returns:
        _type_: _description_
    """
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
    """获取登录用户对象
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()

def login_required(view):
    """判断用户是否登录

    Args:
        view (_type_): _description_

    Returns:
        _type_: _description_
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view