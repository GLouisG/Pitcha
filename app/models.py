from sqlalchemy.orm import backref
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
  pp_path = db.Column(db.String())
  pitch = db.relationship('Pitch', backref='user', lazy=True)
  comment = db.relationship('Comment',backref='user')
  user_vote = db.relationship('Vote', backref='user', lazy='dynamic')

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
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(255))
  content = db.Column(db.String)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  post_time = db.Column(db.DateTime, default=datetime.utcnow)
  comments = db.relationship('Comment', backref='pitch', lazy=True)
  votes = db.relationship('Vote', backref = 'pitch', lazy=True)

  def save_pitch(self):
        db.session.add(self)
        db.session.commit()

  @classmethod
  def get_category(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

  def __repr__(self):
        return f'Pitch{self.text}'

class Vote(db.Model):
  __tablename__='votes'
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
  user = db.relationship("User", backref=backref("votes", cascade="all, delete-orphan"))#removed db.b--
  post_id = db.Column(db.Integer, db.ForeignKey("post.id"), primary_key=True)
  post = db.relationship("Post", backref=backref("votes", cascade="all, delete-orphan"))#remove db.b--
  vo_val = db.Column(db.Boolean, nullable=False)
  
class Comment(db.Model):
  __tablename__='comments'    
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  comment = db.Column(db.String(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))    
  
  def save_comment(self):
        db.session.add(self)
        db.session.commit()

  @classmethod
  def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id)
        return comments
    
  def __repr__(self):
        return f'Comment:{self.comment}'