from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": "Aaron99"})
    password = PasswordField('Mot de passe', validators=[InputRequired()], render_kw={"placeholder": "*******"})
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)], render_kw={"placeholder": "Example@example.com"})
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Aaron99"})
    password = PasswordField('Mot de passe', validators=[InputRequired(), Length(min=8, max=80)], render_kw={"placeholder": "*******"})
    remember = BooleanField('remember me')