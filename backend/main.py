from fastapi import FastAPI
from .routes import workouts, recommendations

app = FastAPI()

# Include API routes
app.include_router(workouts.router, prefix="/workouts")
app.include_router(recommendations.router, prefix="/recommendations")

@app.get("/")
def root():
    return {"message": "Workout AI Backend Running"}
