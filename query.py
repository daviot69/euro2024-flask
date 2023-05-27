from models.base import Session, Country, Venue
from sqlalchemy.sql import select

session = Session()

countries = session.query(Country).all()
for country in countries:
    print(country.country_name)

# venues = session.query(Venue).join(Country, Venue.country_id).all()
# for venue in venues:
#     print(f"{venue.venue_name} is in {venue.city}")

for v, c in session.query(Venue, Country).filter(Venue.country_id == Country.id).all():
    print(f"{v.venue_name} is in the City of {v.city}, {c.country_name}")
