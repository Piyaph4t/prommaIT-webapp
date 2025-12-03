from flask import Flask
from app.extensions import db, login_manager, admin
from config import Config

__FLASK_APP__ = Flask(__name__)

def create_app(config_class=Config):
    global __FLASK_APP__
    __FLASK_APP__.config.from_object(config_class)

    # Initialize Extensions
    db.init_app(__FLASK_APP__)
    login_manager.init_app(__FLASK_APP__)

    # Initialize Admin
    admin.init_app(__FLASK_APP__)


    # Import Models and Views for Admin
    from app.models import User, Student
    from app.admin_views import SecureModelView, StudentView

    # Add Views to Admin
    # Use StudentView for Student (to get image upload)
    admin.add_view(StudentView(Student, db.session))
    admin.add_view(SecureModelView(User, db.session))
    return __FLASK_APP__


# User Loader for Flask-Login
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# Route URL
from app import routes