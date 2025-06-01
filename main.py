from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import aura  # your main API endpoints

app = FastAPI(
    title="Aura Game API",
    description="Backend API for Aura — a game of self-growth and environmental reflection.",
    version="1.0.0"
)

# CORS Middleware - allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route files
app.include_router(aura.router, prefix="/api/aura")

@app.get("/")
def read_root():
    return {"message": "Aura Backend is running 🚀"}
