# 🌱 AgentDock Eco Planner

**AgentDock Eco Planner** is a sustainable route planning platform designed to help users minimize carbon emissions by selecting eco-friendly routes. It integrates AI agents into a docking station (**AgentDock**) using **Cequence AI** for secure authentication and tool access.

---

## 🚀 Live Deployment

- **Frontend**: [https://ai-eco.onrender.com/](https://ai-eco.onrender.com/)  
- **Backend**: [https://ai-eco-backendd.onrender.com](https://ai-eco-backendd.onrender.com)  

---

## 🧩 Features

- 🌍 Interactive **map interface** (Leaflet + React)  
- ⚡ Real-time **eco-route suggestions** with carbon footprint estimates  
- 🤖 AI-powered **route optimization** with sustainability in mind  
- 🛠️ **AgentDock integration** → allowing AI agents to interact securely  
- 🔐 **Authentication & Security via Cequence AI**  
- 🚀 Scalable backend powered by **FastAPI**  

---

## 🏗️ Architecture

![Architecture Diagram](.<img width="1983" height="1545" alt="AIECO_Theme2_ArchitectureDiagram" src="https://github.com/user-attachments/assets/d0bc51e1-636a-49e7-a8a8-f076b209509f" />
) <!-- replace with actual diagram path -->

### Flow:
1. User interacts with **Frontend (React + Vite)**  
2. Requests are sent to **Backend (FastAPI)**  
3. Backend fetches **route data + sustainability metrics**  
4. AI Agents (via **AgentDock**) plug into tools using **Cequence AI secure MCP Gateway**  
5. Optimized **eco-friendly routes** are returned to the user  

---

## 🔄 Dataflow Diagram

![Dataflow Diagram](.<img width="2320" height="2825" alt="diagram-export-9-10-2025-1_01_13-PM" src="https://github.com/user-attachments/assets/3d030ce7-a07f-42db-b6a7-561ba22d3a8a" />
) <!-- replace with actual diagram path -->

### Step-by-step Dataflow:
1. **User Input**: Origin + Destination entered on frontend  
2. **Frontend → Backend**: Request sent via Axios  
3. **Backend**: Processes request, queries AI/route APIs  
4. **Cequence AI Authentication**: Ensures secure agent access  
5. **Response**: Optimized eco-route with carbon footprint sent back to frontend  
6. **Frontend Display**: Results shown on interactive map  

---

## 🔐 Authentication with Cequence AI

We are using **Cequence AI’s MCP Gateway** to:  
- ✅ Secure **API endpoints** for agent-to-server interactions  
- ✅ Protect against **unauthorized agent access**  
- ✅ Enable **real-time session validation** for AI agents  
- ✅ Provide **per-user tool access control**  

This ensures that only trusted AI agents can dock into **AgentDock** and interact with our eco-route planner.  

📸 *Screenshot of Cequence AI Authentication Flow:*  
![Cequence AI Screenshot](.<img width="959" height="415" alt="cequencesai" src="https://github.com/user-attachments/assets/4f868041-ad39-413c-8755-00007fe80938" />
) <!-- replace with actual screenshot -->


---

## 📸 Application Screenshots

### 🌍 Eco Route Map  
![Eco Route Screenshot](<img width="960" height="470" alt="testrout1" src="https://github.com/user-attachments/assets/2398d35a-0735-4dd0-b102-e737350e801a" />
) <!-- replace with actual screenshot -->
![Eco Route Screenshot](<img width="379" height="415" alt="testroutereport2" src="https://github.com/user-attachments/assets/846f0466-ec75-4e34-9d05-ae7ca5fb65bf" />

) <!-- replace with actual screenshot -->

![Eco Route Screenshot](<img width="616" height="400" alt="testfinal5" src="https://github.com/user-attachments/assets/c278ee64-6db2-4aae-8078-4876437e68f4" />


) <!-- replace with actual screenshot -->

### 🔐 Cequence AI AgentDock Access  
![Cequence AgentDock Screenshot](<img width="956" height="418" alt="cequencesai2" src="https://github.com/user-attachments/assets/dcc20923-3201-4356-a3f6-419353d33510" />
) <!-- replace with actual screenshot -->

---

## ⚙️ Tech Stack

- **Frontend**: React + Vite + TailwindCSS + Leaflet  
- **Backend**: FastAPI + Uvicorn  
- **AI Agent Security**: Cequence AI (MCP Gateway)  
- **Deployment**: Render (Frontend + Backend)  
- **Visualization**: Lucide-react, React-Leaflet  

---

## 📌 Future Enhancements

- ✅ Carbon footprint comparison across multiple routes  
- ✅ Integration with **public transport APIs**  
- ✅ User accounts + trip history (with Cequence AI auth)  
- ✅ Advanced analytics for sustainability tracking  

---

## Features

🌱 **Eco-Scoring Algorithm**: Intelligent scoring system that evaluates routes based on:
- Transportation mode efficiency
- Real-time air quality conditions
- Weather impact on travel
- Distance optimization
- CO2 emissions calculation

🗺️ **Multi-Modal Route Planning**: Compare different transportation options:
- Walking
- Cycling
- Driving
- Custom route preferences

🌤️ **Real-Time Environmental Data**:
- Weather conditions via OpenWeather API
- Air quality index and pollution levels
- Dynamic recommendations based on current conditions

  **Architecture Diagram**
  https://claude.ai/public/artifacts/d9f685b7-a071-4694-b8c0-8c2e94cb9efa?fullscreen=true
  

## API Endpoints

### Core Eco-Planning

- `GET /eco/plan` - Comprehensive route planning with eco-scoring
- `GET /eco/compare` - Quick comparison of all transportation modes

### Individual Data Sources

- `GET /weather` - Real-time weather data
- `GET /pollution` - Air quality and pollution information  
- `GET /route` - Basic route calculation

### Health Check

- `GET /healthz` - API health status

## Example Usage

### Plan an Eco-Friendly Route

```bash
GET /eco/plan?start=80.2707,13.0827&end=80.2430,13.0674&modes=driving-car,cycling-regular,foot-walking
```

**Response includes:**
- Ranked route options by eco-score
- Detailed environmental analysis
- CO2 emissions calculations
- Personalized recommendations
- Weather and air quality conditions

### Quick Route Comparison

```bash
GET /eco/compare?start=80.2707,13.0827&end=80.2430,13.0674
```

**Returns simplified comparison** of all transportation modes with key metrics.

## Eco-Scoring Methodology

The eco-score (0-100) considers:

1. **Transportation Mode** (40% weight)
   - Walking/Cycling: 95-100 points
   - Driving: 30 points
   - Heavy vehicles: 15 points

2. **Air Quality Impact** (25% weight)
   - Good AQI (1-2): Bonus points
   - Poor AQI (4-5): Penalty points

3. **Distance Efficiency** (20% weight)
   - Shorter routes receive bonus points
   - Long routes get distance penalty

4. **Weather Conditions** (15% weight)
   - Favorable weather: Bonus for outdoor modes
   - Poor weather: Penalty for walking/cycling

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
ORS_API_KEY=your_openrouteservice_key
OPENWEATHER_API_KEY=your_openweather_key
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Visit `/docs` when the server is running to access the interactive Swagger documentation.

## Environmental Impact

This application promotes sustainable transportation by:
- Encouraging walking and cycling over driving
- Providing real-time air quality awareness
- Calculating and displaying CO2 emissions
- Offering weather-appropriate travel recommendations
- Helping users make informed, eco-conscious travel decisions



✨ Built with ❤️ by **Swetha Ganesh**  
