import requests
import time

API_URL = "https://healthstats-api.example.com/records"
API_KEY = "free_tier_key_abc123"

records = []

for page in range(1, 101):
    response = requests.get(API_URL, params={"page": page, "key": API_KEY})
    
    if response.status_code != 200:
        break  # Stop if API fails
    
    data = response.json()
    records.extend(data.get("results", []))
    
    time.sleep(1)  # Respect rate limit (1 request/sec)
