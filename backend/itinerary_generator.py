import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-1.5-flash")

def generate_itinerary(destination, duration, interests):

    prompt = f"""
    Create a detailed {duration}-day travel itinerary for {destination}.
    The traveler is interested in: {interests}.
    
    Include:
    - Daily activities
    - Suggested restaurants
    - Travel tips
    - Approximate budget suggestions
    """

    response = model.generate_content(prompt)
    return response.text