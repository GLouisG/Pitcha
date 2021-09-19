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
    food = Pitch.filter_by(category='Food')
    innovative = Pitch.filter_by(category='Innovative')
    return render_template('index.html', peaches=pitches, ent = entertainment, food = food, innovative=innovative)    

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    pitch = Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        comment =form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(pitch_id=pitch_id,comment=comment, user_id=user_id,)
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)
    
    