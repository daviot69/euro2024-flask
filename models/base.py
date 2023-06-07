import sqlalchemy
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    ForeignKey,
    Select,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime
from flask_login import UserMixin

engine = create_engine(
    "mariadb+mariadbconnector://db_admin:Krakow1068@192.168.1.12:3306/euro2024"
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class WildcardGroup(Base):
    __tablename__ = "wildcard_groups"
    id = Column(Integer, primary_key=True)
    wildcard_group_name = Column(String(length=20), nullable=False)
    points_bonus = Column(Integer, nullable=False)
    points_penalty = Column(Integer, nullable=False)
    countries = relationship("Country", backref="wildcard_group", lazy=True)

    def __int__(self, wildcard_group_name, points_bonus, points_penalty):
        self.wildcard_group_name = wildcard_group_name
        self.points_bonus = points_bonus
        self.points_penalty = points_penalty


class Stage(Base):
    __tablename__ = "stages"
    id = Column(Integer, primary_key=True)
    stage_description = Column(String(length=50), nullable=False)
    matches = relationship("Match", backref="stage")

    def __int__(self, stage_description):
        self.stage_description = stage_description


class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key=True)
    venue_name = Column(String(length=50), nullable=False)
    city = Column(String(length=50), nullable=False)
    country_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False
    )
    matches = relationship("Match", backref="venue")

    def __int__(self, venue_name, city, country_id):
        self.venue_name = venue_name
        self.city = city
        self.country_id = country_id


class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    forename = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    email_address = Column(String(length=100), nullable=False, unique=True)
    favourite_club_id = Column(
        Integer, ForeignKey("clubs.id", ondelete="CASCADE"), nullable=False
    )
    administrator = Column(Boolean, default=False, nullable=False)
    password_hash = Column(String(length=200), nullable=False)
    creation_date = Column(DateTime, default=datetime.now())
    last_updated_date = Column(DateTime)

    def __int__(
        self, forename, surname, email_address, favourite_club_id, administrator
    ):
        self.forename = forename
        self.surname = surname
        self.email_address = email_address
        self.favourite_club_id = favourite_club_id
        self.administrator = administrator


# TODO Change user_id to be user_entry_id and change relationship
class MatchPrediction(Base):
    __tablename__ = "match_predictions"
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    match_id = Column(
        Integer, ForeignKey("matches.id", ondelete="CASCADE"), nullable=False
    )
    home_score_prediction = Column(Integer, nullable=True)
    away_score_prediction = Column(Integer, nullable=True)
    prediction_points = Column(Integer, default=0, nullable=False)
    wildcard_team_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=True
    )
    wildcard_bonus_points = Column(Integer, default=0, nullable=False)
    wildcard_penalty_points = Column(Integer, default=0, nullable=False)

    match = relationship("Match", foreign_keys="MatchPrediction.match_id")
    # match = relationship("Match", backref="match_id", lazy=True)


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    match_date = Column(DateTime, nullable=False)
    venue_id = Column(Integer, ForeignKey("venues.id"), nullable=False)
    stage_id = Column(Integer, ForeignKey("stages.id"), nullable=False)
    home_team_id = Column(Integer, ForeignKey("countries.id"), nullable=True)
    away_team_id = Column(Integer, ForeignKey("countries.id"), nullable=True)
    home_score = Column(Integer, nullable=True)
    away_score = Column(Integer, nullable=True)
    extra_time = Column(Boolean, nullable=False, default=False)
    penalties = Column(Boolean, nullable=False, default=False)
    home_penalties = Column(Integer, nullable=True)
    away_penalties = Column(Integer, nullable=True)

    home_country = relationship("Country", foreign_keys="Match.home_team_id")
    away_country = relationship("Country", foreign_keys="Match.away_team_id")

    def __int__(self, match_date, venue_id, stage_id, home_team_id, away_team_id):
        self.match_date = match_date
        self.venue_id = venue_id
        self.stage_id = stage_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id


class UserEntry(Base):
    __tablename__ = "user_entries"
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    wildcard_team_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=True
    )
    num_wildcard_changes = Column(Integer, default=0, nullable=False)
    total_goals_prediction = Column(Integer, nullable=True)
    creation_date = Column(DateTime, default=datetime.now())
    last_updated_date = Column(DateTime, nullable=True)
    entry_fee_paid = Column(Boolean, default=False)


class Club(Base):
    __tablename__ = "clubs"
    id = Column(Integer, primary_key=True)
    club_name = Column(String(length=100), nullable=False)

    def __int__(self, club_name):
        self.club_name = club_name


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String(length=100), nullable=False)
    country_shortcode = Column(String(length=10), nullable=False)
    wildcard_group_id = Column(Integer, ForeignKey("wildcard_groups.id"))

    def __int__(self, country_name, country_shortcode, wildcard_group_id):
        self.country_name = country_name
        self.country_shortcode = country_shortcode
        self.wildcard_group_id = wildcard_group_id
