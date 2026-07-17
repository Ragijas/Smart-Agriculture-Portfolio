def read_sensor_value(raw_value):
    try:
        value = float(raw_value)
        print(f"Reading successful: {value}")
        return value
    except ValueError:
        print(f"Error: '{raw_value}' is not a valid sensor reading.")
        return None
    
read_sensor_value("24.5")  # Valid reading
read_sensor_value("ERROR_NO_SIGNAL")   # Invalid reading

def calculate_average(readings):
    try:
        return sum(readings) / len(readings)
    except ZeroDivisionError:
        print("Error: No readings to average.")
        return None
    
print(calculate_average([24.5, 25.0, 23.8]))  # Valid readings
print(calculate_average([]))  # No readings

def close_connection():
    try:
        # Simulating closing a connection
        print("Reading sensor data...")
        raise ConnectionError("Sensor disconnected.")
    except ConnectionError as e:
        print(f"Error: {e}")
    finally:
        print("Connection closed (always runs).")
        
close_connection()