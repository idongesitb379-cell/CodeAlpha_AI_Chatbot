from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

# Serve the HTML page
@app.get("/")
def home():
    return FileResponse("index.html")

# Chat endpoint
@app.post("/chat")
async def chat(data: Message):
    user_message = data.message.lower()

    if "pricing" in user_message or "price" in user_message:
        reply = "Our pricing starts at $50 per month."

    elif "support" in user_message:
        reply = "Our support team is available 24/7."

    elif "hours" in user_message:
        reply = "We are open Monday to Friday from 9 AM to 5 PM."

    elif "services" in user_message:
        reply = "We provide web development, cloud solutions, and technical support."

    elif "contact" in user_message:
        reply = "You can contact us at support@company.com."

    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! Welcome to our customer support service."

    else:
        reply = "Sorry, I didn't understand that. Please ask about pricing, support, services, hours, or contact information."

    return {"response": reply}