from fastapi import APIRouter
from pydantic import BaseModel
from services.conversation import process_message

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    return process_message(req.session_id, req.message)
