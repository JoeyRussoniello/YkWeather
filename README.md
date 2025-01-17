# YKWeather API Caller

This project fetches weather forecast data from the Met.no API for a list of coordinates and processes the data into a CSV file.

## Project Structure
```sh
├── README.md             #This file.
├── coords.csv            #Input file containing the list of areas with their respective latitude and longitude.
├── main.py               #Main script to fetch and process weather data.
└── weather_forecasts.csv #Output file containing the processed weather data.
```

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

You can install the required libraries using pip:

```sh
pip install requests pandas
```

## Usage
1. Prepare the coords.csv file with the following columns
    1. `Area`: Name of the area
    2. `Latitude`: Latitude of the area
    3. `Longitude`: Longitude of the area
2. Run the `main.py` script:
```sh
python main.py
```
3. The scripts will read the coordinates from `coords.csv`, fetch the weather data from the Met.no API, process the data, and save it to `weather_forecasts.csv`.
### Example `coords.csv`
| Area       | Latitude | Longitude |
|------------|----------|-----------|
| Oslo       | 59.9139  | 10.7522   |
| Bergen     | 60.3913  | 5.3221    |
| Trondheim  | 63.4305  | 10.3951   |

### Example Output `weather_forecasts.csv`
| Area       | ForecastTime         | Time                  | AirTemperature (°C) | CloudFraction (%) | RelativeHumidity (%) | WindDirection (°) | WindSpeed (m/s) | NextHourSummary | Precipitation (mm) |
|------------|----------------------|-----------------------|----------------------|-------------------|-----------------------|-------------------|-----------------|-----------------|---------------------|
| Oslo       | 2023-10-01T12:00:00Z | 2023-10-01T13:00:00Z  | 15.0                | 75.0              | 60.0                  | 180.0             | 5.0             | clearsky        | 0.0                 |
| Bergen     | 2023-10-01T12:00:00Z | 2023-10-01T13:00:00Z  | 14.0                | 80.0              | 70.0                  | 190.0             | 4.0             | partlycloudy    | 0.1                 |
| Trondheim  | 2023-10-01T12:00:00Z | 2023-10-01T13:00:00Z  | 13.0                | 85.0              | 80.0                  | 200.0             | 3.0             | cloudy          | 0.2                 |
