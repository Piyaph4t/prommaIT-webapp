from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'admin.login_view' # Redirect to admin login if needed
admin = Admin(name='Promma Admin', template_mode='bootstrap4')
