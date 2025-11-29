from flask import Flask
from config import Config
from app.extensions import db, login_manager, admin
from app.models import User, Student, Award
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class SecureModelView(ModelView):
    def is_accessible(self):
        # In a real app, strict this to: return current_user.is_authenticated
        # For setup testing, we allow it, but recommend enabling auth later
        return True 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    # Add Admin Views
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Student, db.session))
    admin.add_view(SecureModelView(Award, db.session))

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Create DB and Admin User
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            print("Creating default admin user...")
            u = User(username='admin')
            u.set_password('admin123')
            db.session.add(u)
            db.session.commit()

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
