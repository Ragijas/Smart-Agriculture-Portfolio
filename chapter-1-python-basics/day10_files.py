with open("sensor_log.txt", "w") as file:
    file.write("Day 10 - Sensor log started\n")
    file.write("Temperature: 24.5\n")
    file.write("Humidity: 65.0\n")

print("\n--- Written to sensor_log.txt ---\n")

with open("sensor_log.txt", "r") as file:
    content = file.read()
    print("--- Reading from sensor_log.txt ---")
    print(content)

readings = [
    ("2026-07-18 09:00", 24.5, 65.0),
    ("2026-07-18 10:00", 25.1, 63.2),
    ("2026-07-18 11:00", 26.0, 60.5),
]

with open("sensor_data.csv", "w") as file:
    file.write("timestamp,temperature,humidity\n")
    for row in readings:
        file.write(f"{row[0]},{row[1]},{row[2]}\n")

print("--- Written to sensor_data.csv ---")

with open("sensor_data.csv", "r") as file:
    for line in file:
        print(line.strip())