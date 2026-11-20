# Week 1.3, Session 2: Home Sensor Filtering

home_sensors = {
    "Living Room Thermostat": 85,
    "Front Door Lock": 15,
    "Kitchen Smoke Detector": 90,
    "Basement Flood Sensor": 8
}

# Dictionary comprehension to filter sensors with battery below 20
low_battery = {sensor: battery for sensor, battery in home_sensors.items() if battery < 20}

# Print the new dictionary
print(low_battery)
