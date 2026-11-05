import random
import time

# Simulate reading the temperature sensor
def read_sensor():
    return round(random.uniform(20.0, 32.0), 1)

# Simple Edge logic: threshold judgment
for i in range(5):
    temp = read_sensor()
    if temp > 28:
        print(f"[ALERT] High temp detected: {temp}°C")
    else:
        print(f"[Normal] Temp: {temp}°C")
    time.sleep(1)
