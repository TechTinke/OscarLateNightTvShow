import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Seed users
        user = User(username='admin')
        user.set_password('password')
        db.session.add(user)
        
        # Seed guests
        guest1 = Guest(name='Praise Victoria', occupation='Actor')
        guest2 = Guest(name='Oscar Maingi', occupation='Comedian')
        db.session.add_all([guest1, guest2])
        
        # Seed episodes
        episode1 = Episode(date=date(2025, 6, 1), number=1)
        episode2 = Episode(date=date(2025, 6, 2), number=2)
        db.session.add_all([episode1, episode2])
        
        # Seed appearances
        appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
        appearance2 = Appearance(rating=5, guest_id=2, episode_id=1)
        db.session.add_all([appearance1, appearance2])
        
        db.session.commit()
        print('Database seeded successfully!')

if __name__ == '__main__':
    seed_data()