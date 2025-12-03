import os
from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from wtforms.validators import DataRequired
from flask_admin.model.form import InlineFormAdmin
from app.models import Contact
class ContactInline(InlineFormAdmin):
    form_label = 'Contact Info'
    form_columns = ('id', 'platform', 'address')
    form_args = {
        'platform': {
            'label': 'Platform Name (Key)',
            'render_kw': {'placeholder': 'e.g. Facebook, Discord'}
        },
        'address': {
            'label': 'Username/URL (Value)',
            'render_kw': {'placeholder': 'e.g. user_handle'}
        }
    }
# 1. Base View: Restricts access to logged-in users
class SecureModelView(ModelView):
    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        # Redirect to login page if not logged in
        return redirect(url_for('login', next=request.url))

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
    inline_models = (ContactInline(Contact),)

    column_list = ('name', 'school_gmail', 'contacts')

    # Optional: Formats the contacts list nicely in the main table
    def _format_contacts(view, context, model, name):
        return ", ".join([str(c) for c in model.contacts])

    column_formatters = {
        'contacts': _format_contacts

        # Customizing the list view in Admin
    }



    # 1. Define the Inline view for Contacts


# 2. Add it to the Student View
