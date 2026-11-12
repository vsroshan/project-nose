
"""
Project NOSE
Simulated gas sensor data generator.

These readings are synthetic test data.
They do not represent real-world gas measurements.
"""

import random
from datetime import datetime, timezone


def generate_reading():
    """Generate one simulated environmental sensor reading."""

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sensor_id": "NOSE-SIM-001",
        "source": "simulation",
        "simulated": True,
        "temperature_c": round(random.uniform(23.0, 30.0), 2),
        "humidity_percent": round(random.uniform(35.0, 70.0), 2),
        "pressure_hpa": round(random.uniform(990.0, 1020.0), 2),
        "gas_resistance_ohms": round(
            random.uniform(10000.0, 500000.0), 2
        ),
    }


if __name__ == "__main__":
    reading = generate_reading()

    print("PROJECT NOSE — SENSOR SIMULATOR")
    print("-" * 40)

    for key, value in reading.items():
        print(f"{key}: {value}")
