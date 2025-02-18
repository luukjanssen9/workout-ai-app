from fastapi import APIRouter
from pydantic import BaseModel
from ..database import save_workout

router = APIRouter()

class WorkoutLog(BaseModel):
    user_id: int
    exercise: str
    muscle_group: str
    sets: int
    reps: int
    weight: float

@router.post("/log")
def log_workout(workout: WorkoutLog):
    save_workout(workout.dict())
    return {"message": "Workout logged successfully"}
