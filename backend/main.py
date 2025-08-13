from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from llm.llm_handler import LLMHandler
from helpers.cloudflare import run_cloudflare_tunnel
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI(title="Local LLM API")
url = run_cloudflare_tunnel()
print(url)
origins = [
    "http://127.0.0.1:5000",  # Your frontend URL (change accordingly)
    url,
    # Add any other allowed origins
]

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM once when server starts
llm = LLMHandler()

# Define request schema
class ChatRequest(BaseModel):
    text: str

# Define response schema (optional but good practice)
class ChatResponse(BaseModel):
    response: str


@app.post("/summarize", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    # Pass the text to your LLM
    output = llm.summarize(request.text)  # You can replace with run_agent() later
    return ChatResponse(response=output)

# Mount the frontend directory as static files at the root URL
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    # Run API locally
    uvicorn.run(app, host="0.0.0.0", port=5000)
