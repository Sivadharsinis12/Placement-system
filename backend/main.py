from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_data():
    with open("data.json") as f:
        return json.load(f)

@app.get("/")
def root():
    return {"message": "Placement System API"}

@app.post("/login")
def login(user: dict):
    data = read_data()
    for u in data["users"]:
        if u["email"] == user["email"] and u["password"] == user["password"]:
            return {"success": True, "user": u}
    return {"success": False}

@app.get("/dashboard")
def get_dashboard():
    data = read_data()
    return data["dashboard"]

@app.get("/activities")
def get_activities():
    data = read_data()
    return data["activities"]

@app.get("/profile")
def get_profile():
    data = read_data()
    return data["profile"]

@app.get("/history")
def get_history():
    data = read_data()
    return data["history"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
