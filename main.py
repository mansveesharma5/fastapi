from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# Request model
class MessagePayload(BaseModel):
    session_id: str
    message: str

# Store chats by session
sessions: Dict[str, List[Dict[str, str]]] = {}

# Load history for a specific session
@app.get("/chat/load-history/{session_id}")
def load_history(session_id: str):

    # Create session if not exists
    if session_id not in sessions:
        sessions[session_id] = [
            {
                "sender": "bot",
                "text": "Hello! How can I help you today?"
            }
        ]

    return {
        "status": "success",
        "history": sessions[session_id]
    }

# Send message
@app.post("/chat/message")
def send_message(payload: MessagePayload):

    session_id = payload.session_id

    # Create session if not exists
    if session_id not in sessions:
        sessions[session_id] = []

    # Save user message
    sessions[session_id].append({
        "sender": "user",
        "text": payload.message
    })

    # Bot reply
    bot_reply = f"Received your message: '{payload.message}'"

    # Save bot reply
    sessions[session_id].append({
        "sender": "bot",
        "text": bot_reply
    })

    return {
        "status": "success",
        "reply": bot_reply,
        "history": sessions[session_id]
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)




# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Dict

# app = FastAPI()

# # Matches your frontend payload structure
# class MessagePayload(BaseModel):
#     message: str

# # Aligned mock database: Changed "message" key to "text" to match your UI mapping!
# chat_history: List[Dict[str, str]] = [
#     {"sender": "bot", "text": "Hello! How can I help you today?"}
# ]

# @app.get("/chat/load-history")
# def load_history():
#     """Returns the chat history list matching frontend property names."""
#     return {"status": "success", "history": chat_history}

# @app.post("/chat/message")
# def send_message(payload: MessagePayload):
#     """Receives a user message, stores it, and returns a response matching the UI."""
#     # 1. Save user message to history using 'text'
#     chat_history.append({"sender": "user", "text": payload.message})
    
#     # 2. Simulate a basic bot reply
#     bot_reply = f"Received your message: '{payload.message}'"
#     chat_history.append({"sender": "bot", "text": bot_reply})
    
#     return {
#         "status": "success",
#         "user_message": payload.message,
#         "reply": bot_reply # Handled dynamically by handleSubmit in ChatWindow
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Dict, List

# app = FastAPI()

# # =========================
# # REQUEST MODEL
# # =========================

# class MessagePayload(BaseModel):
#     session_id: str
#     message: str


# # =========================
# # SESSION DATABASE
# # =========================

# sessions: Dict[str, Dict] = {

#     "1": {

#         "title": "Main Chat Room",

#         "messages": [

#             {
#                 "sender": "bot",
#                 "text": "Hello! How can I help you today?"
#             }

#         ]
#     }
# }


# # =========================
# # LOAD ALL SESSIONS
# # =========================

# @app.get("/chat/sessions")
# def load_sessions():

#     formatted_sessions = []

#     for session_id, session_data in sessions.items():

#         formatted_sessions.append({

#             "id": session_id,

#             "title": session_data["title"],

#             "messages": session_data["messages"]

#         })

#     return {

#         "status": "success",

#         "sessions": formatted_sessions

#     }


# # =========================
# # CREATE NEW SESSION
# # =========================

# @app.post("/chat/create-session")
# def create_session():

#     new_id = str(len(sessions) + 1)

#     sessions[new_id] = {

#         "title": f"New Chat {new_id}",

#         "messages": []

#     }

#     return {

#         "status": "success",

#         "session": {

#             "id": new_id,

#             "title": sessions[new_id]["title"],

#             "messages": []

#         }

#     }


# # =========================
# # LOAD SINGLE SESSION
# # =========================

# @app.get("/chat/session/{session_id}")
# def load_single_session(session_id: str):

#     if session_id not in sessions:

#         return {

#             "status": "error",

#             "message": "Session not found"

#         }

#     return {

#         "status": "success",

#         "session": {

#             "id": session_id,

#             "title": sessions[session_id]["title"],

#             "messages": sessions[session_id]["messages"]

#         }

#     }


# # =========================
# # SEND MESSAGE
# # =========================

# @app.post("/chat/message")
# def send_message(payload: MessagePayload):

#     session_id = payload.session_id

#     if session_id not in sessions:

#         return {

#             "status": "error",

#             "message": "Invalid session"

#         }

#     # USER MESSAGE
#     sessions[session_id]["messages"].append({

#         "sender": "user",

#         "text": payload.message

#     })

#     # BOT REPLY
#     bot_reply = f"Received your message: '{payload.message}'"

#     sessions[session_id]["messages"].append({

#         "sender": "bot",

#         "text": bot_reply

#     })

#     return {

#         "status": "success",

#         "reply": bot_reply

#     }


# # =========================
# # RUN SERVER
# # =========================

# if __name__ == "__main__":

#     import uvicorn

#     uvicorn.run(
#         app,
#         host="127.0.0.1",
#         port=8000
#     )



# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List, Dict

# app = FastAPI()

# # Matches your frontend payload structure
# class MessagePayload(BaseModel):
#     message: str

# # Aligned mock database: Changed "message" key to "text" to match your UI mapping!
# chat_history: List[Dict[str, str]] = [
#     {"sender": "bot", "text": "Hello! How can I help you today?"}
# ]

# @app.get("/chat/load-history")
# def load_history():
#     """Returns the chat history list matching frontend property names."""
#     return {"status": "success", "history": chat_history}

# @app.post("/chat/message")
# def send_message(payload: MessagePayload):
#     """Receives a user message, stores it, and returns a response matching the UI."""
#     # 1. Save user message to history using 'text'
#     chat_history.append({"sender": "user", "text": payload.message})
    
#     # 2. Simulate a basic bot reply
#     bot_reply = f"Received your message: '{payload.message}'"
#     chat_history.append({"sender": "bot", "text": bot_reply})
    
#     return {
#         "status": "success",
#         "user_message": payload.message,
#         "reply": bot_reply # Handled dynamically by handleSubmit in ChatWindow
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)



# import os
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd


# app = FastAPI()
# CSV_FILE = "data.csv"

# #Schema for adding new_data via POST
# class Employee(BaseModel):
#     id: int
#     name: str
#     role: str
#     department: str

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# #1. GET Method: Read and return CSV data
# @app.get("/csv-data")
# def get_csv_data():
#     if not os.path.exists(CSV_FILE):
#         raise HTTPException(status_code=404, detail="CSV file not found")
    
#     #Read CSV and convert to a list of dictionaries
#     df = pd.read_csv(CSV_FILE)
#     return df.to_dict(orient="records")

# #2. POST Method: Receive data and append to CSV
# @app.post("/csv-data")
# def add_csv_data(employee: Employee):
#         #Prepare the new row
#         new_data = pd.DataFrame([employee.model_dump()])

#         #Append to existing CSV or create a new one
#         if os.path.exists(CSV_FILE):
#             new_data.to_csv(CSV_FILE, mode="a", header=False, index=False)
#         else:
#             new_data.to_csv(CSV_FILE, mode="w", header=True, index=False)
#         return {"message": "Data added successfully", "data": employee}
    
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}



