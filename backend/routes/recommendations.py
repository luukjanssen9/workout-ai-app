from fastapi import APIRouter
from ..models.recommendations import recommend_exercises

router = APIRouter()

@router.get("/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommend_exercises(user_id)
    return {"recommendations": recommendations}
