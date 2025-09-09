from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import weather, pollution, route, eco_planner

app = FastAPI(title="Eco-MCP API", version="1.0")

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # use ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(pollution.router, prefix="/pollution", tags=["Pollution"])
app.include_router(route.router, prefix="/route", tags=["Route"])
app.include_router(eco_planner.router, prefix="/eco", tags=["Eco Planning"])

@app.get("/healthz")
def health_check():
    return {"status": "ok", "message": "Eco-MCP API is running"}
