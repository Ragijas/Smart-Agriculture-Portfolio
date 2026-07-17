humidity = 35
if humidity < 40:
    print("The humidity is low - watering needed")
elif humidity > 70:
    print("The humidity is high - skip watering")
else:
    print("The humidity is normal")

print("\n--- Simulating 5 sensor reading ---")
for i in range(5):
    print(f"Reading {i + 1}: humidity = {humidity + i}")
print("\n--- Watering cycle simulation ---")
count = 0
while count < 3:
    print(f"Watering cycle {count + 1} in progress...")
    count += 1
print("Watering completed.")