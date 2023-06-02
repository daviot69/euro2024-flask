from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models.base import Session, Club, Country


class RegistrationForm(FlaskForm):
    forename = StringField("Forename", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    email_address = StringField("Email", validators=[DataRequired(), Email(message="Please Enter a Valid Email Address")])
    favourite_club_id = SelectField("Favourite Club")
    favourite_country_id = SelectField("Favourite Country")
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('password_check', message='Passwords Must Match')])
    password_check = PasswordField("Confirm Password", validators=[DataRequired()])

    submit = SubmitField("Register")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        session = Session()
        #self.favourite_club_id.choices = [("", "Pick your Team")]
        self.favourite_club_id.choices = [(club.id, club.club_name) for club in session.query(Club).order_by(Club.club_name).all()]
        self.favourite_country_id.choices = [(country.id, country.country_name) for country in session.query(Country).order_by(Country.country_name).all()]
        session.close()


class LoginForm(FlaskForm):
    email_address = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")
