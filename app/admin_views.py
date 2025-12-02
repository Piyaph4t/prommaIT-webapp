import os
from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from wtforms.validators import DataRequired

# 1. Base View: Restricts access to logged-in users
class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # Redirect to login page if not logged in
        return redirect(url_for('main.login', next=request.url))

# 2. Student View: Adds Image Upload Logic
class StudentView(SecureModelView):
    # Determine the path for uploads
    file_path = os.path.join(os.path.dirname(__file__), 'static', 'images')

    # Override the 'image_url' field to be a File Upload field
    form_extra_fields = {
        'image_url': ImageUploadField(
            'Profile Image',
            base_path=file_path,       # Where to save the file
            url_relative_path='images/', # How to access it in HTML
            namegen=None               # Keep original filename (optional)
        )
    }

    # Customizing the list view in Admin
    column_list = ('name', 'school_gmail', 'image_url')