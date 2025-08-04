
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so your frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for incoming messages
class ChatRequest(BaseModel):
    messages: list

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.messages[-1]["content"].lower()

    # Branded Responses
    if "who developed you" in user_message or "your developer" in user_message:
        return {"response": "I was developed by Laurixy. The founder and CEO is SheikhZada Haris."}

    if "who is the founder of laurixy" in user_message:
        return {"response": "The founder and CEO of Laurixy is SheikhZada Haris."}

    if "what is laurixy" in user_message:
        return {"response": "Laurixy is a global AI and software company that builds futuristic tools for people worldwide."}

    # Default reply if no custom question matched
    return {"response": "Sorry, I can't answer that yet. Laurixy AI is learning more every day!"}
