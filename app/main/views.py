from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User, Pitch, Comment, Vote
from flask_login import login_required, current_user
from .forms import EditProfile, PitchForm, CommentForm
from .. import db, photos



main.route('/')
def index():
    pitches = Pitch.query.all()
    entertainment = Pitch.filter_by(category='Entertainment')
    entertainment = Pitch.filter_by(category='Food')
    entertainment = Pitch.filter_by(category='Innovative')
    
    