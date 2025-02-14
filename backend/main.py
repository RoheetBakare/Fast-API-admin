from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Fake user data (for testing)
fake_users = {"bakareroheet@gmail.com": "password123"}

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    if request.email in fake_users and fake_users[request.email] == request.password:
        return {"message": "Login successful", "token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
