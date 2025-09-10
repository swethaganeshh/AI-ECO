from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.server.fastapi import FastAPIMCP

from app.routes import weather, pollution, route, eco_planner

app = FastAPI(title="Eco-MCP API", version="1.0")

# --- CORS configuration ---
origins = [
    "https://ai-eco.onrender.com",  # your React frontend (no trailing slash)
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # use ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include existing REST routes ---
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(pollution.router, prefix="/pollution", tags=["Pollution"])
app.include_router(route.router, prefix="/route", tags=["Route"])
app.include_router(eco_planner.router, prefix="/eco", tags=["Eco Planning"])

# --- MCP setup ---
mcp = FastAPIMCP(app)

# Define MCP tools
@mcp.tool("eco_plan", description="Plan an eco-friendly route")
async def eco_plan(start: str, end: str, modes: str = "driving-car,cycling-regular,foot-walking"):
    # Ideally call your existing /eco/planner logic here
    return {
        "start": start,
        "end": end,
        "modes": modes,
        "status": "planned"
    }

@mcp.tool("eco_compare", description="Compare eco routes between two points")
async def eco_compare(start: str, end: str):
    # Ideally call your /eco/compare logic here
    return {
        "start": start,
        "end": end,
        "comparison": "results"
    }

# --- Health check ---
@app.get("/healthz")
def health_check():
    return {"status": "ok", "message": "Eco-MCP API is running"}
