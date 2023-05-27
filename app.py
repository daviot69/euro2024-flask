from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms.user_forms import RegistrationForm
from models.base import Session, User

# Create a Flask Instance
app = Flask(__name__)
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "mysql+pymysql://db_admin:Krakow1068@192.168.1.12:3306/users"

app.config["SECRET_KEY"] = "SidSidSid"

# db = SQLAlchemy(app)


# # CreateModel
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow())
#
#     def __repr__(self):
#         return "<Name %r" % self.name


# with app.app_context():
#     db.create_all()


# # Create a Form Class
# class UserForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired()])
#     submit = SubmitField("Submit")


# # Create a Form Class
# class NamerForm(FlaskForm):
#     name = StringField("What's Your Name", validators=[DataRequired()])
#     submit = SubmitField("Submit")


# Create a route decorator
@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 404


# @app.route("/name", methods=["GET", "POST"])
# def name():
#     name = None
#     form = NamerForm()
#     # Validate Form
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ""
#         flash("Form Submitted Successfully")
#     return render_template("name.html", name=name, form=form)


# @app.route("/user/add", methods=["GET", "POST"])
# def add_user():
#     name = None
#     form = UserForm()
#     if form.validate_on_submit():
#         user = Users.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = Users(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ""
#         form.email.data = ""
#     our_users = Users.query.order_by(Users.date_added)
#     return render_template("add_user.html", name=name, our_users=our_users, form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session = Session()
        user = (
            session.query(User)
            .filter(User.email_address == form.email_address.data)
            .first()
        )
        if not user:
            session.add(
                User(
                    email_address=form.email_address.data,
                    forename=form.forename.data,
                    surname=form.surname.data,
                    favourite_club_id=form.favourite_club_id.data,
                    favourite_country_id=form.favourite_country_id.data
                    # wildcard_country_id=1,
                )
            )
            session.commit()
            session.close()
            flash(f"Registered Successfully - Welcome {form.forename.data}")
        else:
            flash("This Email Address is already Registered")
    return render_template("register.html", form=form)
