from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models import User, Student
from app.main import bp


@bp.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            # Redirect to Admin if that's where they wanted to go
            next_page = request.args.get('next')
            return redirect(next_page or '/admin')
        else:
            flash('Invalid username or password')

    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))