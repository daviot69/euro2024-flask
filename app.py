from flask import Flask, render_template, flash, redirect, url_for
from forms.user_forms import RegistrationForm, LoginForm
from models.base import Session, User, WildcardGroup, Match
from flask_bcrypt import Bcrypt
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user,
)

# Create a Flask Instance
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user


bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "SidSidSid"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/scoring")
def scoring():
    return render_template("scoring.html")


@app.route("/wildcard_groups")
def wildcard_groups():
    session = Session()
    wildcard_group_details = (
        session.query(WildcardGroup).order_by(WildcardGroup.wildcard_group_name).all()
    )

    return render_template(
        "wildcard_groups.html", wildcard_group_details=wildcard_group_details
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


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
            pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            session.add(
                User(
                    email_address=form.email_address.data,
                    forename=form.forename.data,
                    surname=form.surname.data,
                    favourite_club_id=form.favourite_club_id.data,
                    password_hash=pw_hash,
                )
            )
            session.commit()
            session.close()
            flash("Registered Successfully - Please Log In")
            return redirect(url_for("login"))
        else:
            flash("This Email Address is already Registered")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = Session()
        user = (
            session.query(User)
            .filter(User.email_address == form.email_address.data)
            .first()
        )
        if user:
            if bcrypt.check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for("dashboard"))
            else:
                flash("Incorrect Password - Try again")
        else:
            flash("No Account exists with this Email Address")

    return render_template("login.html", form=form)


@app.route("/user_profile", methods=["GET", "POST"])
@login_required
def user_profile():
    return render_template("user_profile.html")


@app.route("/predictions", methods=["GET", "POST"])
@login_required
def predictions():
    session = Session()
    match_details = session.query(Match).order_by(Match.match_date).all()
    return render_template("predictions.html", match_details=match_details)


@app.route("/dashboard")
@login_required
def dashboard():
    session = Session()
    upcoming_fixtures = (
        session.query(Match)
        .filter_by(home_score=None)
        .order_by(Match.match_date)
        .limit(6)
        .all()
    )

    latest_results = (
        session.query(Match)
        .filter(Match.home_score >= 0)
        .order_by(Match.match_date)
        .limit(6)
        .all()
    )

    # latest_results = (
    #     session.query(Match)
    #     .order_by(Match.match_date)
    #     .filter_by(Match.home_score is not None)
    # )
    return render_template(
        "dashboard.html",
        upcoming_fixtures=upcoming_fixtures,
        latest_results=latest_results,
    )


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been Logged Out")
    return redirect(url_for("login"))
