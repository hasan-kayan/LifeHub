import json
import secrets
from datetime import datetime, timedelta
import time

# Function to generate a new secret key
def generate_secret_key():
    return secrets.token_hex(32)  # Generate a 256-bit (32-byte) key

# Function to update the JSON file with a new secret key
def update_json_file(json_file_path, new_secret_key):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    data['appSecretKey'] = new_secret_key
    
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Your JSON file path
json_file_path = 'config.json'

# Generate and update a new secret key five times a day
for _ in range(5):
    new_secret_key = generate_secret_key()
    update_json_file(json_file_path, new_secret_key)
    print(f"Updated appSecretKey to: {new_secret_key}")
    
    # Wait for one day before generating the next key
    # Adjust the sleep time as needed
    one_day = timedelta(days=1)
    today = datetime.now().date()
    tomorrow = today + one_day
    next_run_time = datetime.combine(tomorrow, datetime.min.time())
    time_until_next_run = next_run_time - datetime.now()
    
    if time_until_next_run.total_seconds() > 0:
        time.sleep(time_until_next_run.total_seconds())
