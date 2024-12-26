from fasthtml.common import database

# Path to the database file
DB_PATH = 'data/my_app.db'
db = database(DB_PATH)

# Define table shortcuts
country, governorate, city, user_profile, conference, user_conference = (
    db.t.country,
    db.t.governorate,
    db.t.city,
    db.t.user_profile,
    db.t.conference,
    db.t.user_conference,  # For the many-to-many relationship
)

def initialize_db():
    # Enable foreign key enforcement
    db.execute('PRAGMA foreign_keys = ON')

    # Create country table
    if 'country' not in db.t:
        country.create(dict(id=int, name=str), pk='id')

    # Create governorate table
    if 'governorate' not in db.t:
        governorate.create(
            dict(id=int, name=str, country=int),
            pk='id',
            foreign_keys={'country': 'country.id'}
        )

    # Create city table
    if 'city' not in db.t:
        city.create(
            dict(id=int, name=str, governorate=int),
            pk='id',
            foreign_keys={'governorate': 'governorate.id'}
        )

    # Create user_profile table
    if 'user_profile' not in db.t:
        user_profile.create(
            dict(
                id=int,
                name=str,
                email=str,
                city=int,
            ),
            pk='id',
            foreign_keys={'city': 'city.id'}
        )

    # Create conference table
    if 'conference' not in db.t:
        conference.create(
            dict(
                id=int,
                name=str,
                date=str,
                path=str,
            ),
            pk='id'
        )

    # Create user_conference table
    if 'user_conference' not in db.t:
        user_conference.create(
            dict(
                user_profile=int,
                conference=int,
            ),
            foreign_keys={
                'user_profile': 'user_profile.id',
                'conference': 'conference.id',
            }
        )

def get_all_conferences():
    # Fetch all rows from the 'conference' table
    rows = conference.all()  # Returns a list of dictionaries or dataclasses
    return rows

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully!")

