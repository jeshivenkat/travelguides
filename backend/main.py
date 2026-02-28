from fastapi import FastAPI
from pydantic import BaseModel
from itinerary_generator import generate_itinerary
from fastapi.middleware.cors import CORSMiddleware
from models import save_itinerary, get_all_itineraries

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelRequest(BaseModel):
    destination: str
    duration: int
    interests: str

@app.post("/generate")
def create_itinerary(request: TravelRequest):
    itinerary = generate_itinerary(
        request.destination,
        request.duration,
        request.interests
    )
    # Save to DB
    save_itinerary(request.destination, request.duration, request.interests, itinerary)
    return {"itinerary": itinerary}

@app.get("/history")
def history():
    return get_all_itineraries()
