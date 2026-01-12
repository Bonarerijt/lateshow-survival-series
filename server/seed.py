import csv

from app import app
from models import db, Episode, Guest, Appearance

def seed_data():
    with app.app_context():

        print("Clearing existing data...")
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        db.session.commit()

        episode_map = {}
        episode_counter = 1

        with open('seed.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Episode (use Show as date)
                show_date = row['Show']

                if show_date not in episode_map:
                    episode = Episode(
                        date=show_date,
                        number=episode_counter
                    )
                    db.session.add(episode)
                    db.session.commit()

                    episode_map[show_date] = episode
                    episode_counter += 1
                else:
                    episode = episode_map[show_date]

                # Guest
                guest_name = row['Raw_Guest_List']

                guest = Guest.query.filter_by(name=guest_name).first()
                if not guest:
                    guest = Guest(
                        name=guest_name,
                        occupation=row['GoogleKnowlege_Occupation']
                    )
                    db.session.add(guest)
                    db.session.commit()

                # Appearance (CSV has no rating → default)
                appearance = Appearance(
                    rating=3,
                    episode_id=episode.id,
                    guest_id=guest.id
                )

                db.session.add(appearance)

            db.session.commit()

        print("✅ Database seeded successfully from CSV!")

if __name__ == "__main__":
    seed_data()