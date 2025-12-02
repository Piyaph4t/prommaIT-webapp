import os
from dotenv import load_dotenv

load_dotenv()
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'a095d1e3f865381318f2c5f692a330e4e58411dfab275c3e58e33eb38c94f302'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')

    # Configure Upload Folder (pointing to app/static/images)
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'images')