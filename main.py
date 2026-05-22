from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Matches your frontend payload structure
class MessagePayload(BaseModel):
    message: str

# Aligned mock database: Changed "message" key to "text" to match your UI mapping!
chat_history: List[Dict[str, str]] = [
    {"sender": "bot", "text": "Hello! How can I help you today?"}
]

@app.get("/chat/load-history")
def load_history():
    """Returns the chat history list matching frontend property names."""
    return {"status": "success", "history": chat_history}

@app.post("/chat/message")
def send_message(payload: MessagePayload):
    """Receives a user message, stores it, and returns a response matching the UI."""
    # 1. Save user message to history using 'text'
    chat_history.append({"sender": "user", "text": payload.message})
    
    # 2. Simulate a basic bot reply
    bot_reply = f"Received your message: '{payload.message}'"
    chat_history.append({"sender": "bot", "text": bot_reply})
    
    return {
        "status": "success",
        "user_message": payload.message,
        "reply": bot_reply # Handled dynamically by handleSubmit in ChatWindow
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



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



