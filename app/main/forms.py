from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    biog = TextAreaField('We would like to know more about you.',validators = [Required()])
    submit = SubmitField('Save')
class PitchForm(FlaskForm):
    category = SelectField('Category', choices=[('Food','Food'),('Entertainment','Entertainment'),('Innovative','Innovative')],validators=[Required()])
    content = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Please leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
