from flask import Blueprint, render_template
from app.models import Student
from app.main import bp

@bp.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
