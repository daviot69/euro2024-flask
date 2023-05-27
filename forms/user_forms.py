from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    email_address = StringField("Email", validators=[DataRequired()])
    forename = StringField("Forename", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    favourite_club_id = StringField("Favourite Club")
    favourite_country_id = StringField("Favourite Country")

    submit = SubmitField("Register")
