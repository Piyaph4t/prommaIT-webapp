from sqlalchemy.orm import backref
from wtforms.validators import length

from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    awards = db.relationship('Award', backref='student', lazy=True)
    school_gmail = db.Column(db.String(length=120),unique=True,nullable=False)
    contacts = db.relationship('Contact', backref='student', lazy='dynamic', cascade="all, delete-orphan")



class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)

    # 🎯 The Foreign Key (The Anchor)
    # This links the contact record back to the specific student.
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False, index=True)

    # 🌟 Dynamic Fields (For optional platforms like FB, IG, Personal Gmail)
    platform = db.Column(db.String(50), nullable=False) # e.g., "Facebook", "IG", "Personal_Gmail"
    address = db.Column(db.String(200), nullable=False) # e.g., "john.doe.profile", "johndoe@gmail.com"

    # Composite Index for faster lookups of a specific platform for a specific student
    __table_args__ = (
        db.Index('idx_student_platform', student_id, platform),
    )

class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
