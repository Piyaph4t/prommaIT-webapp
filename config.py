import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'c25241542e5fdc57023c2e2467e15069dae4fa457f0b9f4c7db0612857165fd9'  # Change this!
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')

    # Configure Upload Folder (pointing to app/static/images)
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'images')