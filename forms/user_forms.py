from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    IntegerField,
    SelectField,
    SubmitField,
    HiddenField,
    Form,
    FormField,
    FieldList,
)
from wtforms.validators import (
    ValidationError,
    InputRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)
from models.base import Session, Club, Country


class RegistrationForm(FlaskForm):
    forename = StringField(
        "Forename", validators=[InputRequired(message="Please enter your First Name")]
    )
    surname = StringField("Surname", validators=[InputRequired()])
    email_address = StringField(
        "Email",
        validators=[
            InputRequired(),
            Email(message="Please Enter a Valid Email Address"),
        ],
    )
    favourite_club_id = SelectField("Favourite Club")
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            EqualTo("password_check", message="Passwords Must Match"),
            Length(min=6, message="Password must be at least 6 characters"),
        ],
    )
    password_check = PasswordField("Confirm Password", validators=[InputRequired()])

    submit = SubmitField("Register")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        session = Session()
        # self.favourite_club_id.choices = [("", "Pick your Team")]
        self.favourite_club_id.choices = [
            (club.id, club.club_name)
            for club in session.query(Club).order_by(Club.club_name).all()
        ]

        session.close()


class LoginForm(FlaskForm):
    email_address = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

    submit = SubmitField("Login")


class MatchPrediction(Form):
    prediction_id = HiddenField()
    match_id = HiddenField()
    home_score = IntegerField(validators=[InputRequired(), NumberRange(min=0)])
    away_score = IntegerField(validators=[InputRequired(), NumberRange(min=0)])


class PredictionForm(FlaskForm):
    total_goals = IntegerField(
        "Total Goals in Tournament (not including Penalty Shootouts)",
        validators=[InputRequired(), NumberRange(min=0)],
    )
    wildcard_team_id = SelectField("Wildcard Team")
    prediction = FieldList(FormField(MatchPrediction), max_entries=36)
    # submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        session = Session()
        # self.wildcard_team_id.choices = [("", "Pick your Wildcard Team")]
        self.wildcard_team_id.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.wildcard_team_id.choices.append((0, "No Selection"))
        session.close()
