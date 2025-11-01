from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateProjectForm(FlaskForm):
    title = StringField('Project Title', 
                       validators=[DataRequired(), Length(min=2, max=100)])
    
    description = TextAreaField('Project Description',
                              validators=[DataRequired(), Length(min=10, max=1000)])
    
    category = SelectField('Category', 
                          choices=[
                              ('web', 'Web Development'),
                              ('mobile', 'Mobile App'),
                              ('ai', 'AI/ML'),
                              ('game', 'Game Development'),
                              ('other', 'Other')
                          ],
                          validators=[DataRequired()])
    
    skills_needed = StringField('Skills Needed',
                              validators=[Length(max=200)],
                              description='Comma-separated skills (e.g., Python, JavaScript, Design)')
    
    submit = SubmitField('Create Project')