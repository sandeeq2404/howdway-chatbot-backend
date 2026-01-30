sessions = {}

def get_session(session_id: str):
    return sessions.get(session_id, {
        "step": "greeting",
        "data": {}
    })

def update_session(session_id: str, session_data: dict):
    sessions[session_id] = session_data

def clear_session(session_id: str):
    sessions.pop(session_id, None)
