from services.session import get_session, update_session, clear_session
from services.firebase import save_consultation

BUSINESS_CATEGORIES = [
    "Technology", "Cafe", "Restaurant", "Finance", "E-commerce",
    "Food Business", "Agriculture", "Vertical Farming", "Healthcare",
    "Education", "Manufacturing", "Real Estate", "Logistics", "Other"
]

def process_message(session_id: str, user_message: str):
    session = get_session(session_id)
    step = session["step"]
    data = session["data"]

    if step == "greeting":
        session["step"] = "service"
        update_session(session_id, session)
        return {
            "message": "Great! What services are you looking for?",
            "buttons": ["Web/App Development", "Chatbot Development", "Digital Marketing", "Other"]
        }

    elif step == "service":
        data["service"] = user_message
        session["step"] = "name"
        update_session(session_id, session)
        return {"message": "May I know your name?"}

    elif step == "name":
        data["name"] = user_message
        session["step"] = "phone"
        update_session(session_id, session)
        return {"message": "Could you share your phone number?"}

    elif step == "phone":
        data["phone"] = user_message
        session["step"] = "email"
        update_session(session_id, session)
        return {"message": "Please provide your email address."}

    elif step == "email":
        data["email"] = user_message
        session["step"] = "category"
        update_session(session_id, session)
        return {
            "message": "What is your business category?",
            "buttons": BUSINESS_CATEGORIES
        }

    elif step == "category":
        data["category"] = user_message
        save_consultation(data)
        clear_session(session_id)
        return {
            "message": "Thank you! 🙌 We’ve received your details. Our team will contact you shortly to schedule your free consultation."
        }

    else:
        clear_session(session_id)
        return {"message": "Something went wrong. Please refresh and try again."}
