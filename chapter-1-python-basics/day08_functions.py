def check_humidity(humidity):
    if humidity < 40:
        return "watering needed"
    elif humidity > 70:
        return "skip watering"
    else:
        return "normal humidity"

def read_sensor (name, value):
    print(f"[{name}] reading: {value}")
    return value

result1 = check_humidity(35)
print(f"Humidity 35: {result1}")

result2 = check_humidity(75)
print(f"Humidity 75: {result2}")

temp = read_sensor("DHT22", 24.5)
ph = read_sensor("pH Sensor", 6.2)