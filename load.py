from models.base import (
    Session,
    engine,
    Base,
    Country,
    Club,
    Wildcard_Group,
    Stage,
    Venue,
)

Base.metadata.create_all(engine)
session = Session()

session.add(
    Wildcard_Group(wildcard_group_name="Group 1", points_bonus=10, points_penalty=20)
)
session.add(
    Wildcard_Group(wildcard_group_name="Group 2", points_bonus=15, points_penalty=15)
)
session.add(
    Wildcard_Group(wildcard_group_name="Group 3", points_bonus=20, points_penalty=10)
)
session.add(
    Wildcard_Group(wildcard_group_name="Group 4", points_bonus=25, points_penalty=5)
)


session.add(Country(country_name="Germany", wildcard_group_id=None))
session.add(Country(country_name="Sweden", wildcard_group_id=None))

session.add(Club(club_name="Aston Villa"))
session.add(Club(club_name="Arsenal"))

session.add(Venue(venue_name="Olympiastadion", city="Berlin", country_id=1))
session.add(Venue(venue_name="Cologne Stadium", city="Cologne", country_id=1))
session.add(Venue(venue_name="BVB Stadion", city="Dortmund", country_id=1))
session.add(Venue(venue_name="Düsseldorf Arena", city="Düsseldorf", country_id=1))
session.add(Venue(venue_name="Frankfurt Arena", city="Frankfurt", country_id=1))
session.add(Venue(venue_name="Arena AufSchalke", city="Gelsenkirchen", country_id=1))
session.add(Venue(venue_name="Volksparkstadion", city="Hamburg", country_id=1))
session.add(Venue(venue_name="Leipzig Stadium", city="Leipzig", country_id=1))
session.add(Venue(venue_name="Munich Football Arena", city="Munich", country_id=1))
session.add(Venue(venue_name="Stuttgart Arena", city="Stuttgart", country_id=1))

session.add(Stage(stage_description="Group A"))
session.add(Stage(stage_description="Group B"))
session.add(Stage(stage_description="Group C"))
session.add(Stage(stage_description="Group D"))
session.add(Stage(stage_description="Group E"))
session.add(Stage(stage_description="Group F"))
session.add(Stage(stage_description="Round of 16"))
session.add(Stage(stage_description="Quarter Final"))
session.add(Stage(stage_description="Semi Final"))
session.add(Stage(stage_description="Final"))

session.commit()
session.close()
