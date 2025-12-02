from flask import Flask
from app.extensions import db, login_manager, admin
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Initialize Admin
    admin.init_app(app)

    # Register Blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Import Models and Views for Admin
    from app.models import User, Student, Contact, Award
    from app.admin_views import SecureModelView, StudentView

    # Add Views to Admin
    # Use StudentView for Student (to get image upload)
    admin.add_view(StudentView(Student, db.session))
    # Use SecureModelView for others (just to protect them)
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Contact, db.session))
    admin.add_view(SecureModelView(Award, db.session))

    return app


# User Loader for Flask-Login
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))