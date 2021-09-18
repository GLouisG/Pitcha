from .import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
  __tablename__='users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255),nullable=False, unique=True)
  email = db.Column(db.String(255), nullable=False, unique=True)
  biog = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  pp_path = db.Column(db.String(255))
  # pitch = db.relationship('Pitch', backref='user', lazy=True)
  # comment = db.relationship('Comment',backref='user')
  #user_vote = db.relationship('Vote', backref='author', lazy='dynamic')

  @property
  def password(self):
        raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
        self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

  def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
  __tablename__='pitches'
  #a
class Vote(db.Model):
  __tablename__='votes'
#
class Comment(db.Model):
  __tablename__='comments'           
