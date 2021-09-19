from . import main
from flask import render_template, request, redirect, url_for, abort,flash
from ..models import User, Pitch, Comment, Upvote, Downvote
from flask_login import login_required, current_user
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos



@main.route('/')
def index():
    pitches = Pitch.query.all()
    entertainment = Pitch.query.filter_by(category='Entertainment')
    food = Pitch.query.filter_by(category='Food')
    innovative = Pitch.query.filter_by(category='Innovative')
    return render_template('index.html', pitches=pitches, entertainment=entertainment, food = food, innovative=innovative)    

@main.route('/comment/<int:pitch_id>', methods = ['pitch','GET'])
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
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)
@main.route('/new_pitch', methods = ['pitch','GET'])

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user,pitches=pitches)

@login_required    
def new_pitch():
    form = PitchForm
    if form.validate_on_submit():
        category = form.category.data
        content = form.content.data
        user_id = current_user.get_current_object.id
        new_pitch_obj = Pitch(category=category, content=content, user_id=user_id)
        new_pitch_obj.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)
@main.route('/user/<uname>/update/profile',methods= ['pitch'])
@login_required
def update_picture(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.dp_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))  


@main.route('/like/<int:id>', methods = ['POST', 'GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()     
    return redirect(url_for('main.index',id=id))    

@main.route('/dislike/<int:id>', methods = ['POST','GET'])
@login_required
def dislike(id):
    get_pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pit in get_pitch:
        to_str = f'{pit}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()     
    return redirect(url_for('main.index',id=id))        

@main.route('/user/<uname>/update_profile',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    form = UpdateProfile()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.biog = form.biog.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)    
# @main.route('/vote/<pitch_id>/<vote_action>', methods=['GET'])
# @login_required
# def pitch_vote(pitch_id, vote_action):
#     pitch = Pitch.query.filter_by(id = pitch_id).first_or_404()
#     vote = Vote.query.filter_by(user = current_user,pitch = pitch).first()

#     if vote:
#         if vote.vo_val != bool(int(vote_action)):
#             vote.vo_val = bool(int(vote_action))
#             db.session.commit()
#             return redirect(url_for('main.index', pitch_id = pitch.id))
#         else:
#             flash('You already voted for this pitch')
#             return redirect(url_for('main.index', pitch_id = pitch.id))

#     vote = Vote(user = current_user, pitch = pitch, vo_val = bool(int(vote_action)))
#     db.session.add(vote)
#     db.session.commit()
#     flash('Thanks for voting')
#     upvotes = Vote.get_upvotes(pitch_id, True)
#     downvotes = Vote.get_downvotes(pitch_id, False)
#     return redirect(url_for('main.index', pitch_id = pitch.id))    
    

    
