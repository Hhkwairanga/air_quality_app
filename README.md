# Air Quality Checker

The **Air Quality Checker** is a Flask web application that allows users to input geographical bounding box coordinates (latitude and longitude) and retrieve real-time air quality data for cities within that region. The data includes temperature, humidity, dew point, wind speed, and the Air Quality Index (AQI). This app uses the [World Air Quality Index (WAQI) API](https://waqi.info/) to fetch the data.

## Features

- **Input Bounding Box**: Users can input minimum and maximum latitude/longitude values to define a region.
- **Air Quality Data**: Fetches real-time air quality data for cities within the specified bounding box.
- **Detailed Metrics**: Includes temperature, humidity, dew point, wind speed, and AQI for each city.
- **CSV Export**: Users can download the air quality data as a CSV file.
- **Responsive UI**: Built using Bootstrap 5 for a responsive user interface.

## API Information

The application uses the **World Air Quality Index (WAQI) API** to retrieve real-time air quality data. The API provides air quality information for various locations around the world. You will need an API key from WAQI to use the application.

- API Endpoint: `https://api.waqi.info/map/bounds/`
- API Documentation: [WAQI API Documentation](https://aqicn.org/api/)

## Technologies Used

- **Flask**: Python web framework for building the server-side application.
- **HTML/CSS/Bootstrap 5**: For creating the frontend interface.
- **JavaScript (AJAX)**: For asynchronous form submission and real-time updates.
- **WAQI API**: For fetching real-time air quality data.

## Installation and Setup

Follow these steps to set up and run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/hhkwairanga/air_quality_app.git
cd air_quality_app
```

### 2. Install dependencies

Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
### 3. Set up the WAQI API key

You will need to set up an environment variable for the WAQI API key. You can do this by either using a `.env` file or by exporting the environment variable directly in your shell.

### Using a .env file

Create a `.env` file in the root of your project and add the following line:

```bash
API_KEY=your_waqi_api_key
```
Replace your_waqi_api_key with the actual API key you obtain from WAQI.

### Export environment variable directly (Optional)

Alternatively, you can set the environment variable directly in your terminal by running the following command:

bash

export API_KEY=your_waqi_api_key

### 4. Run the application

Once everything is set up, you can run the Flask application locally with the following command:

```bash
flask run
```
Alternatively, if you prefer to run the application using the default script, use:

```bash
python app.py
```
### 5. Access the application

Open a web browser and navigate to:

http://127.0.0.1:5000/

You should now be able to interact with the Air Quality Checker app locally.
# Usage

### Enter Bounding Box Coordinates

The application requires users to input four values to define a geographical bounding box:

    Latitude Min: The minimum latitude of the bounding box.
    Longitude Min: The minimum longitude of the bounding box.
    Latitude Max: The maximum latitude of the bounding box.
    Longitude Max: The maximum longitude of the bounding box.

### Retrieve Air Quality Data

After entering the bounding box coordinates, click the Get Air Quality button. The app will use the World Air Quality Index (WAQI) API to fetch the air quality data for cities located within the specified region.
#### View the Results

The air quality data, including temperature, humidity, dew point, wind speed, and the air quality index (AQI) for each city, will be displayed in a table.

#### Download CSV

After the air quality data is fetched, a Download CSV button will appear. Clicking this button will allow you to download the displayed data as a CSV file for further analysis.
Example

Here's a basic flow of how the app works:

    Enter Bounding Box: Users input the latitude and longitude bounds.
    Air Quality Data: The app retrieves real-time data for cities within the bounding box and displays it in a table.
    Download CSV: Users can download the air quality data as a CSV file by clicking the Download CSV button.


    The application uses the World Air Quality Index (WAQI) API to retrieve real-time air quality data. We appreciate their service and the data they provide.

### Author

- Haruna Hamidu Kwairanga
- GitHub: [hhkwairanga](https://github.com/Hhkwairanga/)
- Gmail: harunahk5575@gmail.com