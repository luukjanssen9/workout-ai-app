import pandas as pd
from sqlalchemy.orm import Session
from ..database import Workout, SessionLocal

muscle_exercises = {
    "Chest": ["Bench Press", "Push-Ups", "Dips"],
    "Back": ["Pull-Ups", "Bent-over Rows", "Deadlifts"],
    "Legs": ["Squats", "Lunges", "Leg Press"],
    "Shoulders": ["Overhead Press", "Lateral Raises"],
}

def recommend_exercises(user_id):
    db = SessionLocal()
    workouts = db.query(Workout).filter(Workout.user_id == user_id).all()
    db.close()
    
    df = pd.DataFrame([w.__dict__ for w in workouts])
    
    muscle_usage = df.groupby("muscle_group")["sets"].sum().to_dict()
    
    least_trained_muscle = min(muscle_usage, key=muscle_usage.get)
    
    return muscle_exercises.get(least_trained_muscle, ["Try a new full-body workout!"])
