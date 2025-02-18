from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./workouts.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    exercise = Column(String)
    muscle_group = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)

Base.metadata.create_all(bind=engine)

def save_workout(data):
    db = SessionLocal()
    new_workout = Workout(**data)
    db.add(new_workout)
    db.commit()
    db.close()
