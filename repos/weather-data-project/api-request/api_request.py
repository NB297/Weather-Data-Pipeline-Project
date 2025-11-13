import requests
api_key = "c1daaa12bdc16b18874f986cd03dffb6"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

# UNCOMMENT BEFORE DEPLOYMENT
# def fetch_data():
#     print("Fetching weather data from Weatherstack API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise an error for bad status codes
#         print("API response received successfully.")
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-11-13 12:50', 'localtime_epoch': 1763038200, 'utc_offset': '-5.0'}, 'current': {'observation_time': '05:50 PM', 'temperature': 9, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'astro': {'sunrise': '06:41 AM', 'sunset': '04:39 PM', 'moonrise': '12:07 AM', 'moonset': '01:39 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 42}, 'air_quality': {'co': '202.85', 'no2': '13.25', 'o3': '64', 'so2': '3.05', 'pm2_5': '3.25', 'pm10': '3.25', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 28, 'wind_degree': 293, 'wind_dir': 'WNW', 'pressure': 1012, 'precip': 0, 'humidity': 50, 'cloudcover': 100, 'feelslike': 6, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}