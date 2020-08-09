from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
	email = StringField('Email: ', validators=[Email()])
	password = PasswordField('Password: ', validators=[DataRequired(), Length(min=8, max=100)])
	remember = BooleanField('Remember Me: ', default=False)
	submit = SubmitField('Register!')
		