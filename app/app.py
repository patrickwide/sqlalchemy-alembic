from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User

# Replace 'sqlite:///mydatabase.db' with your actual database URL.
engine = create_engine('sqlite:///mydatabase.db')

# Create a session factory bound to the engine.
Session = sessionmaker(bind=engine)

# Create a session.
session = Session()

# new_user = User(username='john_doe', email='john@example.com')
# session.add(new_user)
# session.commit()


user = session.query(User).filter_by(username='john_doe').first()
print(f'User: {user.username}, Email: {user.email}')
