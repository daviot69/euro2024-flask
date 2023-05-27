from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime

engine = create_engine(
    "mariadb+mariadbconnector://db_admin:Krakow1068@192.168.1.12:3306/euro2024"
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Wildcard_Group(Base):
    __tablename__ = "wildcard_groups"
    id = Column(Integer, primary_key=True)
    wildcard_group_name = Column(String(length=20), nullable=False)
    points_bonus = Column(Integer, nullable=False)
    points_penalty = Column(Integer, nullable=False)

    def __int__(self, wildcard_group_name, points_bonus, points_penalty):
        self.wildcard_group_name = wildcard_group_name
        self.points_bonus = points_bonus
        self.points_penalty = points_penalty


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String(length=100), nullable=False)
    wildcard_group_id = Column(
        Integer,
        ForeignKey("wildcard_groups.id", ondelete="CASCADE"),
    )

    def __int__(self, country_name, wildcard_group_id):
        self.country_name = country_name
        self.wildcard_group_id = wildcard_group_id


class Club(Base):
    __tablename__ = "clubs"
    id = Column(Integer, primary_key=True)
    club_name = Column(String(length=100), nullable=False)

    def __int__(self, club_name):
        self.club_name = club_name


class Stage(Base):
    __tablename__ = "stages"
    id = Column(Integer, primary_key=True)
    stage_description = Column(String(length=50), nullable=False)

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
    country = relationship("Country", backref="venues")

    def __int__(self, venue_name, city, country_id):
        self.venue_name = venue_name
        self.city = city
        self.country_id = country_id


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    forename = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    email_address = Column(String(length=100), nullable=False, unique=True)
    favourite_club_id = Column(
        Integer, ForeignKey("clubs.id", ondelete="CASCADE"), nullable=False
    )
    favourite_country_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False
    )
    wildcard_country_id = Column(
        Integer, ForeignKey("countries.id", ondelete="CASCADE")
    )
    creation_date = Column(DateTime, default=datetime.now())

    def __int__(
        self,
        forename,
        surname,
        email_address,
        favourite_club_id,
        favourite_country_id,
        wildcard_country_id
        # creation_date,
    ):
        self.forename = forename
        self.surname = surname
        self.email_address = email_address
        self.favourite_club_id = favourite_club_id
        self.favourite_country_id = favourite_country_id
        self.wildcard_country_id = wildcard_country_id
        # self.creation_date = creation_date
