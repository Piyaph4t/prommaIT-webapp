from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import UniqueConstraint
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




from sqlalchemy import UniqueConstraint


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # 1. FIXED Key (Mandatory)
    school_gmail = db.Column(db.String(120), unique=True, nullable=False)

    # 2. DYNAMIC Dictionary (The Relationship)
    contacts = db.relationship('Contact', backref='student', cascade="all, delete-orphan")


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    # This acts as the "Key" (e.g., 'Facebook', 'Discord')
    platform = db.Column(db.String(50), nullable=False)

    # This acts as the "Value" (e.g., 'john_doe_fb')
    address = db.Column(db.String(200), nullable=False)

    # Dictionary Logic: Prevent duplicate keys for the same student
    __table_args__ = (
        UniqueConstraint('student_id', 'platform', name='unique_student_platform'),
    )

    def __repr__(self):
        return f"{self.platform}: {self.address}"