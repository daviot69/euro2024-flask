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
    user_entry_id = HiddenField()
    total_goals = IntegerField(
        "Total Goals in Tournament (not including Penalty Shootouts)",
        validators=[InputRequired(), NumberRange(min=0)],
    )
    wildcard_team_id = SelectField("Wildcard Team")
    prediction = FieldList(FormField(MatchPrediction), max_entries=36)
    quarter_finalist_1 = SelectField(
        "1st Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_2 = SelectField(
        "2nd Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_3 = SelectField(
        "3rd Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_4 = SelectField(
        "4th Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_5 = SelectField(
        "5th Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_6 = SelectField(
        "6th Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_7 = SelectField(
        "7th Quarter Finalist", validators=[InputRequired()]
    )
    quarter_finalist_8 = SelectField(
        "8th Quarter Finalist", validators=[InputRequired()]
    )
    semi_finalist_1 = SelectField("1st Semi Finalist", validators=[InputRequired()])
    semi_finalist_2 = SelectField("2nd Semi Finalist", validators=[InputRequired()])
    semi_finalist_3 = SelectField("3rd Semi Finalist", validators=[InputRequired()])
    semi_finalist_4 = SelectField("4th Semi Finalist", validators=[InputRequired()])
    finalist_1 = SelectField("1st Finalist", validators=[InputRequired()])
    finalist_2 = SelectField("2nd Finalist", validators=[InputRequired()])
    winner = SelectField("Tournament Winner", validators=[InputRequired()])
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

        self.quarter_finalist_1.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_1.choices.append((0, "No Selection"))

        self.quarter_finalist_2.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_2.choices.append((0, "No Selection"))

        self.quarter_finalist_3.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_3.choices.append((0, "No Selection"))

        self.quarter_finalist_4.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_4.choices.append((0, "No Selection"))

        self.quarter_finalist_5.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_5.choices.append((0, "No Selection"))

        self.quarter_finalist_6.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_6.choices.append((0, "No Selection"))

        self.quarter_finalist_7.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_7.choices.append((0, "No Selection"))

        self.quarter_finalist_8.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.quarter_finalist_8.choices.append((0, "No Selection"))

        self.semi_finalist_1.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.semi_finalist_1.choices.append((0, "No Selection"))

        self.semi_finalist_2.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.semi_finalist_2.choices.append((0, "No Selection"))

        self.semi_finalist_3.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.semi_finalist_3.choices.append((0, "No Selection"))

        self.semi_finalist_4.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.semi_finalist_4.choices.append((0, "No Selection"))

        self.finalist_1.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.finalist_1.choices.append((0, "No Selection"))

        self.finalist_2.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.finalist_2.choices.append((0, "No Selection"))

        self.winner.choices = [
            (country.id, country.country_name)
            for country in session.query(Country).order_by(Country.country_name).all()
        ]
        self.winner.choices.append((0, "No Selection"))

        session.close()
