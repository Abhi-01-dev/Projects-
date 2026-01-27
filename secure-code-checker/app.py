from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from google import genai
from config import PROMPT

load_dotenv()

app = FastAPI(title="Secure Code Checker")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class CodeInput(BaseModel):
    code: str

# Root → Load frontend
@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

# API
@app.post("/analyze")
def analyze_code(data: CodeInput):
    prompt = PROMPT + "\n\nCODE:\n" + data.code

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return {"result": response.text}
