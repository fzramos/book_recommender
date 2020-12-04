from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, TextAreaField, DecimalField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password',\
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

class PreferenceForm(FlaskForm):
    min_rating = DecimalField('Minimum Rating', validators = [DataRequired()])
    # max_rating = DecimalField('Maximum Rating', validators = [DataRequired()])
    book_length = RadioField(
        'Length of Book', 
        choices = ['Short(0-200 pages)', 'Intermediate(200-2000 pages)', 'Long(2000+)', 'Any'],
        validators = [DataRequired()]
    )
    popularity = RadioField(
        'Book Popularity', 
        choices = ['Little Known', 'Popular', 'Very Well-Known'],
        validators = [DataRequired()]
    )
    pub_year = RadioField('Publication Year',
        choices = ['Pre-1997', '1998-2002', '2003-2005', 'Post-2006'])
    # pub_year = IntegerField('Publication Year', validators = [DataRequired()])
    submit = SubmitField()
