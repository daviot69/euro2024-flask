from datetime import datetime
from models.base import (
    Session,
    engine,
    Base,
    Country,
    Club,
    Wildcard_Group,
    Stage,
    Venue,
    Match,
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


session.add(
    Country(country_name="Germany", country_shortcode="GER", wildcard_group_id=None)
)
session.add(
    Country(country_name="Sweden", country_shortcode="SWE", wildcard_group_id=None)
)
session.add(
    Country(country_name="Spain", country_shortcode="SPA", wildcard_group_id=None)
)
session.add(
    Country(country_name="France", country_shortcode="FRA", wildcard_group_id=None)
)
session.add(
    Country(country_name="Portugal", country_shortcode="POR", wildcard_group_id=None)
)
session.add(
    Country(country_name="Wales", country_shortcode="WAL", wildcard_group_id=None)
)
session.add(
    Country(country_name="Scotland", country_shortcode="SCO", wildcard_group_id=None)
)
session.add(
    Country(country_name="England", country_shortcode="ENG", wildcard_group_id=None)
)
session.add(
    Country(country_name="Denmark", country_shortcode="DEN", wildcard_group_id=None)
)
session.add(
    Country(country_name="Holland", country_shortcode="HOL", wildcard_group_id=None)
)
session.add(
    Country(country_name="Belgium", country_shortcode="BEL", wildcard_group_id=None)
)
session.add(
    Country(country_name="Turkey", country_shortcode="TUR", wildcard_group_id=None)
)
session.add(
    Country(country_name="Ukraine", country_shortcode="UKR", wildcard_group_id=None)
)
session.add(
    Country(country_name="Italy", country_shortcode="ITA", wildcard_group_id=None)
)
session.add(
    Country(country_name="Croatia", country_shortcode="CRO", wildcard_group_id=None)
)
session.add(
    Country(country_name="Romania", country_shortcode="ROM", wildcard_group_id=None)
)


session.add(
    Country(country_name="Greece", country_shortcode="GRE", wildcard_group_id=None)
)
session.add(
    Country(
        country_name="Czech Republic", country_shortcode="CZE", wildcard_group_id=None
    )
)
session.add(
    Country(country_name="Poland", country_shortcode="POL", wildcard_group_id=None)
)
session.add(
    Country(country_name="Austria", country_shortcode="AUS", wildcard_group_id=None)
)
session.add(
    Country(country_name="Serbia", country_shortcode="SER", wildcard_group_id=None)
)
session.add(
    Country(country_name="Hungary", country_shortcode="HUN", wildcard_group_id=None)
)
session.add(
    Country(country_name="Slovenia", country_shortcode="SLO", wildcard_group_id=None)
)
session.add(
    Country(country_name="Switzerland", country_shortcode="SWI", wildcard_group_id=None)
)

session.add(Club(club_name="Accrington Stanley"))
session.add(Club(club_name="AFC Wimbledon"))
session.add(Club(club_name="Aldershot Town"))
session.add(Club(club_name="Altrincham"))
session.add(Club(club_name="Arsenal"))
session.add(Club(club_name="Aston Villa"))
session.add(Club(club_name="Barnet"))
session.add(Club(club_name="Barnsley"))
session.add(Club(club_name="Barrow"))
session.add(Club(club_name="Birmingham City"))
session.add(Club(club_name="Blackburn Rovers"))
session.add(Club(club_name="Blackpool"))
session.add(Club(club_name="Bolton Wanderers"))
session.add(Club(club_name="Boreham Wood"))
session.add(Club(club_name="Bournemouth"))
session.add(Club(club_name="Bradford City"))
session.add(Club(club_name="Brentford"))
session.add(Club(club_name="Brighton"))
session.add(Club(club_name="Bristol City"))
session.add(Club(club_name="Bristol Rovers"))
session.add(Club(club_name="Bromley"))
session.add(Club(club_name="Burnley"))
session.add(Club(club_name="Burton Albion"))
session.add(Club(club_name="Cambridge United"))
session.add(Club(club_name="Cardiff City"))
session.add(Club(club_name="Carlisle United"))
session.add(Club(club_name="Charlton Athletic"))
session.add(Club(club_name="Chelsea"))
session.add(Club(club_name="Cheltenham Town"))
session.add(Club(club_name="Chesterfield"))
session.add(Club(club_name="Colchester United"))
session.add(Club(club_name="Coventry City"))
session.add(Club(club_name="Crawley Town"))
session.add(Club(club_name="Crewe Alexandra"))
session.add(Club(club_name="Crystal Palace"))
session.add(Club(club_name="Dagenham & Redbridge"))
session.add(Club(club_name="Derby County"))
session.add(Club(club_name="Doncaster Rovers"))
session.add(Club(club_name="Dorking Wanderers"))
session.add(Club(club_name="Eastleigh"))
session.add(Club(club_name="Everton"))
session.add(Club(club_name="Exeter City"))
session.add(Club(club_name="Fleetwood Town"))
session.add(Club(club_name="Forest Green Rovers"))
session.add(Club(club_name="Fulham"))
session.add(Club(club_name="Gateshead"))
session.add(Club(club_name="Gillingham"))
session.add(Club(club_name="Grimsby Town"))
session.add(Club(club_name="Halifax Town"))
session.add(Club(club_name="Harrogate Town"))
session.add(Club(club_name="Hartlepool United"))
session.add(Club(club_name="Huddersfield Town"))
session.add(Club(club_name="Hull City"))
session.add(Club(club_name="Ipswich Town"))
session.add(Club(club_name="Leeds United"))
session.add(Club(club_name="Leicester City"))
session.add(Club(club_name="Leyton Orient"))
session.add(Club(club_name="Lincoln City"))
session.add(Club(club_name="Liverpool"))
session.add(Club(club_name="Luton Town"))
session.add(Club(club_name="Maidenhead United"))
session.add(Club(club_name="Maidstone United"))
session.add(Club(club_name="Manchester City"))
session.add(Club(club_name="Manchester United"))
session.add(Club(club_name="Mansfield Town"))
session.add(Club(club_name="Middlesbrough"))
session.add(Club(club_name="Millwall"))
session.add(Club(club_name="Milton Keynes Dons"))
session.add(Club(club_name="Morecambe"))
session.add(Club(club_name="Newcastle United"))
session.add(Club(club_name="Newport County"))
session.add(Club(club_name="Northampton Town"))
session.add(Club(club_name="Norwich City"))
session.add(Club(club_name="Nottingham Forest"))
session.add(Club(club_name="Notts County"))
session.add(Club(club_name="Oldham Athletic"))
session.add(Club(club_name="Oxford United"))
session.add(Club(club_name="Peterborough United"))
session.add(Club(club_name="Plymouth Argyle"))
session.add(Club(club_name="Port Vale"))
session.add(Club(club_name="Portsmouth"))
session.add(Club(club_name="Preston North End"))
session.add(Club(club_name="Queens Park Rangers"))
session.add(Club(club_name="Reading"))
session.add(Club(club_name="Rochdale"))
session.add(Club(club_name="Rotherham United"))
session.add(Club(club_name="Salford City"))
session.add(Club(club_name="Scunthorpe United"))
session.add(Club(club_name="Sheffield United"))
session.add(Club(club_name="Sheffield Wednesday"))
session.add(Club(club_name="Shrewsbury Town"))
session.add(Club(club_name="Solihull Moors"))
session.add(Club(club_name="Southampton"))
session.add(Club(club_name="Southend United"))
session.add(Club(club_name="Stevenage"))
session.add(Club(club_name="Stockport County"))
session.add(Club(club_name="Stoke City"))
session.add(Club(club_name="Sunderland"))
session.add(Club(club_name="Sutton United"))
session.add(Club(club_name="Swansea City"))
session.add(Club(club_name="Swindon Town"))
session.add(Club(club_name="Torquay United"))
session.add(Club(club_name="Tottenham Hotspur"))
session.add(Club(club_name="Tranmere Rovers"))
session.add(Club(club_name="Walsall"))
session.add(Club(club_name="Watford"))
session.add(Club(club_name="Wealdstone"))
session.add(Club(club_name="West Bromwich Albion"))
session.add(Club(club_name="West Ham United"))
session.add(Club(club_name="Wigan Athletic"))
session.add(Club(club_name="Woking"))
session.add(Club(club_name="Wolverhampton Wanderers"))
session.add(Club(club_name="Wrexham"))
session.add(Club(club_name="Wycombe Wanderers"))
session.add(Club(club_name="Yeovil Town"))
session.add(Club(club_name="York City"))


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

session.add(
    Match(
        match_date="2024-06-14 20:00",
        venue_id=9,
        stage_id=1,
        home_team_id=1,
        away_team_id=2,
    )
)
session.add(
    Match(
        match_date="2024-06-15 20:00",
        venue_id=1,
        stage_id=2,
        home_team_id=5,
        away_team_id=6,
    )
)
session.add(
    Match(
        match_date="2024-06-15 20:00",
        venue_id=3,
        stage_id=2,
        home_team_id=7,
        away_team_id=8,
    )
)
session.add(
    Match(
        match_date="2024-06-15 20:00",
        venue_id=2,
        stage_id=1,
        home_team_id=3,
        away_team_id=4,
    )
)
session.add(
    Match(
        match_date="2024-06-16 20:00",
        venue_id=6,
        stage_id=3,
        home_team_id=11,
        away_team_id=12,
    )
)
session.add(
    Match(
        match_date="2024-06-16 20:00",
        venue_id=7,
        stage_id=4,
        home_team_id=13,
        away_team_id=14,
    )
)
session.add(
    Match(
        match_date="2024-06-16 20:00",
        venue_id=10,
        stage_id=3,
        home_team_id=9,
        away_team_id=10,
    )
)
session.add(
    Match(
        match_date="2024-06-17 20:00",
        venue_id=4,
        stage_id=4,
        home_team_id=15,
        away_team_id=16,
    )
)
session.add(
    Match(
        match_date="2024-06-17 20:00",
        venue_id=5,
        stage_id=5,
        home_team_id=17,
        away_team_id=18,
    )
)
session.add(
    Match(
        match_date="2024-06-17 20:00",
        venue_id=9,
        stage_id=5,
        home_team_id=19,
        away_team_id=20,
    )
)
session.add(
    Match(
        match_date="2024-06-18 20:00",
        venue_id=8,
        stage_id=6,
        home_team_id=23,
        away_team_id=24,
    )
)
session.add(
    Match(
        match_date="2024-06-18 20:00",
        venue_id=3,
        stage_id=6,
        home_team_id=21,
        away_team_id=22,
    )
)
session.add(
    Match(
        match_date="2024-06-19 20:00",
        venue_id=7,
        stage_id=2,
        home_team_id=6,
        away_team_id=8,
    )
)
session.add(
    Match(
        match_date="2024-06-19 20:00",
        venue_id=2,
        stage_id=1,
        home_team_id=2,
        away_team_id=4,
    )
)
session.add(
    Match(
        match_date="2024-06-19 20:00",
        venue_id=10,
        stage_id=1,
        home_team_id=1,
        away_team_id=3,
    )
)
session.add(
    Match(
        match_date="2024-06-20 20:00",
        venue_id=6,
        stage_id=3,
        home_team_id=5,
        away_team_id=7,
    )
)
session.add(
    Match(
        match_date="2024-06-20 20:00",
        venue_id=5,
        stage_id=2,
        home_team_id=10,
        away_team_id=12,
    )
)
session.add(
    Match(
        match_date="2024-06-20 20:00",
        venue_id=9,
        stage_id=3,
        home_team_id=9,
        away_team_id=11,
    )
)
session.add(
    Match(
        match_date="2024-06-21 20:00",
        venue_id=1,
        stage_id=4,
        home_team_id=13,
        away_team_id=15,
    )
)
session.add(
    Match(
        match_date="2024-06-21 20:00",
        venue_id=8,
        stage_id=4,
        home_team_id=14,
        away_team_id=16,
    )
)
session.add(
    Match(
        match_date="2024-06-21 20:00",
        venue_id=4,
        stage_id=5,
        home_team_id=18,
        away_team_id=20,
    )
)
session.add(
    Match(
        match_date="2024-06-22 20:00",
        venue_id=7,
        stage_id=6,
        home_team_id=22,
        away_team_id=24,
    )
)
session.add(
    Match(
        match_date="2024-06-22 20:00",
        venue_id=3,
        stage_id=6,
        home_team_id=21,
        away_team_id=23,
    )
)
session.add(
    Match(
        match_date="2024-06-22 20:00",
        venue_id=2,
        stage_id=5,
        home_team_id=17,
        away_team_id=19,
    )
)
session.add(
    Match(
        match_date="2024-06-23 20:00",
        venue_id=5,
        stage_id=1,
        home_team_id=4,
        away_team_id=1,
    )
)
session.add(
    Match(
        match_date="2024-06-23 20:00",
        venue_id=10,
        stage_id=1,
        home_team_id=2,
        away_team_id=3,
    )
)
session.add(
    Match(
        match_date="2024-06-24 20:00",
        venue_id=8,
        stage_id=2,
        home_team_id=6,
        away_team_id=7,
    )
)
session.add(
    Match(
        match_date="2024-06-24 20:00",
        venue_id=4,
        stage_id=2,
        home_team_id=8,
        away_team_id=1,
    )
)
session.add(
    Match(
        match_date="2024-06-25 20:00",
        venue_id=1,
        stage_id=4,
        home_team_id=14,
        away_team_id=15,
    )
)
session.add(
    Match(
        match_date="2024-06-25 20:00",
        venue_id=3,
        stage_id=4,
        home_team_id=16,
        away_team_id=13,
    )
)
session.add(
    Match(
        match_date="2024-06-25 20:00",
        venue_id=2,
        stage_id=3,
        home_team_id=12,
        away_team_id=9,
    )
)
session.add(
    Match(
        match_date="2024-06-25 20:00",
        venue_id=9,
        stage_id=3,
        home_team_id=10,
        away_team_id=11,
    )
)
session.add(
    Match(
        match_date="2024-06-26 20:00",
        venue_id=7,
        stage_id=6,
        home_team_id=24,
        away_team_id=21,
    )
)
session.add(
    Match(
        match_date="2024-06-26 20:00",
        venue_id=6,
        stage_id=6,
        home_team_id=22,
        away_team_id=23,
    )
)
session.add(
    Match(
        match_date="2024-06-26 20:00",
        venue_id=5,
        stage_id=5,
        home_team_id=18,
        away_team_id=19,
    )
)
session.add(
    Match(
        match_date="2024-06-26 20:00",
        venue_id=10,
        stage_id=5,
        home_team_id=20,
        away_team_id=17,
    )
)

session.commit()

session.add(Match(match_date="2024-06-29 20:00", venue_id=3, stage_id=7))
session.add(Match(match_date="2024-06-29 20:00", venue_id=1, stage_id=7))
session.add(Match(match_date="2024-06-30 20:00", venue_id=2, stage_id=7))
session.add(Match(match_date="2024-06-30 20:00", venue_id=6, stage_id=7))
session.add(Match(match_date="2024-07-01 20:00", venue_id=5, stage_id=7))
session.add(Match(match_date="2024-07-01 20:00", venue_id=4, stage_id=7))
session.add(Match(match_date="2024-07-02 20:00", venue_id=9, stage_id=7))
session.add(Match(match_date="2024-07-02 20:00", venue_id=8, stage_id=7))

session.add(Match(match_date="2024-07-05 20:00", venue_id=10, stage_id=8))
session.add(Match(match_date="2024-07-05 20:00", venue_id=7, stage_id=8))
session.add(Match(match_date="2024-07-06 20:00", venue_id=1, stage_id=8))
session.add(Match(match_date="2024-07-06 20:00", venue_id=4, stage_id=8))

session.add(Match(match_date="2024-07-09 20:00", venue_id=9, stage_id=9))
session.add(Match(match_date="2024-07-10 20:00", venue_id=3, stage_id=9))

session.add(Match(match_date="2024-07-14 20:00", venue_id=1, stage_id=10))

session.commit()
session.close()
