
"""
Project NOSE
Mac-hosted sensor data API.

Accepts structured sensor readings over HTTP.
"""

from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Project NOSE API",
    description="Sensor data collection and communication service",
    version="0.1.0",
)


class SensorReading(BaseModel):
    timestamp: datetime
    sensor_id: str
    source: Literal["simulation", "raspberry_pi"]
    simulated: bool

    temperature_c: float = Field(ge=-40, le=85)
    humidity_percent: float = Field(ge=0, le=100)
    pressure_hpa: float = Field(gt=0)
    gas_resistance_ohms: float = Field(gt=0)


latest_reading = None
reading_history = []


@app.get("/")
def home():
    return {
        "project": "Project NOSE",
        "service": "Sensor Data API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/sensor/readings")
def receive_reading(reading: SensorReading):
    global latest_reading

    latest_reading = reading.model_dump(mode="json")
    reading_history.append(latest_reading)

    return {
        "message": "Sensor reading received",
        "sensor_id": reading.sensor_id,
        "simulated": reading.simulated,
    }


@app.get("/sensor/latest")
def get_latest_reading():
    if latest_reading is None:
        return {"message": "No readings received yet"}

    return latest_reading


@app.get("/sensor/history")
def get_history():
    return {
        "count": len(reading_history),
        "readings": reading_history,
    }
