from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Get the API key from an environment variable
API_KEY = os.environ.get('API_KEY')

# Debug statement
if API_KEY is None:
    print("API_KEY is not set.")
else:
    print(f"API_KEY has been set successfully: {API_KEY}")  # Print the API key


# Function to fetch air quality data based on bounding box input
def fetch_air_quality_data(bbox):
    url = f"https://api.waqi.info/map/bounds/?token={API_KEY}&latlng={bbox}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        air_quality_data = []

        if "data" in data:
            for entry in data["data"]:
                city_name = entry.get("station", {}).get("name", "Unknown")
                lat = entry.get("lat", "N/A")
                lon = entry.get("lon", "N/A")

                # Fetch detailed data for each station
                detail_url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={API_KEY}"
                detail_response = requests.get(detail_url)

                if detail_response.status_code == 200:
                    detail_data = detail_response.json()

                    if "data" in detail_data and detail_data["status"] == "ok":
                        city = detail_data["data"]["city"]["name"]
                        aqi = detail_data["data"]["aqi"]
                        time = detail_data["data"]["time"]["s"]

                        # Extract temperature, humidity, dew point, and wind speed from IAQI
                        iaqi = detail_data["data"].get("iaqi", {})
                        temperature = iaqi.get("t", {}).get("v", "N/A")
                        humidity = iaqi.get("h", {}).get("v", "N/A")
                        dew_point = iaqi.get("dew", {}).get("v", "N/A")
                        wind_speed = iaqi.get("w", {}).get("v", "N/A")

                        air_quality_data.append({
                            "city": city,
                            "temperature": temperature,
                            "humidity": humidity,
                            "dew_point": dew_point,
                            "wind_speed": wind_speed,
                            "aqi": aqi,
                            "time": time
                        })
        return air_quality_data
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_air_quality', methods=['POST'])
def get_air_quality():
    lat_min = request.form.get('lat_min')
    lon_min = request.form.get('lon_min')
    lat_max = request.form.get('lat_max')
    lon_max = request.form.get('lon_max')

    # Create bounding box string
    bbox = f"{lat_min},{lon_min},{lat_max},{lon_max}"

    # Fetch air quality data based on the bounding box
    air_quality_data = fetch_air_quality_data(bbox)

    if air_quality_data is not None:
        return jsonify(air_quality_data)
    else:
        return jsonify({"error": "Failed to fetch air quality data"}), 500


if __name__ == '__main__':
    app.run(debug=True)
