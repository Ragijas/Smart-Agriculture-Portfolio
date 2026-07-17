readings = [35.0, 36.5, 40.2, 38.1, 42.0]

print("--- List example ---")
print(f"All readings: {readings}")
print(f"First reading: {readings[0]}")
print(f"Number of readings: {len(readings)}")

readings.append(45.5)
print(f"After adding new reading: {readings}")

sensor_data = {
    "temperature": 24.5,
    "humidity": 65.0,
    "sensor_name": "DHT22",
    "is_online": True
}
print("--- Dictionary example ---")
print(f"Sensor data: {sensor_data}")
print(f"Temperature: {sensor_data['temperature']}")

sensor_data["ec"] = 1.8
print(f"After adding EC: {sensor_data}")

print("\n--- Looping through dictionary ---")
for key, value in sensor_data.items():
    print(f"{key}: {value}")