import requests
import pandas as pd

CSV_PATH = 'coords.csv'
OUTPUT_PATH = 'weather_forecasts.csv'

def process_entry(entry, area, forecast_time):
    """Process one Timeseries element from the yr API calls

    Args:
        json_entry (dictionary): one element of json timeseries data from the API
    """
    time = entry['time']
    data = entry['data']
    instant = data['instant']['details']
    try:
        properties = {
            "Area": area,
            "ForecastTime": forecast_time,
            "Time":time,
            "AirTemperature (C)":instant['air_temperature'],
            "CloudFraction":instant['cloud_area_fraction'],
            "RelativeHumidity ":instant['relative_humidity'],
            "WindDirection (degrees)":instant['wind_from_direction'],
            "WindSpeed (m/s)":instant['wind_speed'],
            "NextHourSummary":data['next_1_hours']['summary']['symbol_code'],
            "Precipitation (mm)":data['next_1_hours']['details']['precipitation_amount'],
        }
        return properties
    except KeyError:
        return

def process_area(area,lat,lon):
    # Define the endpoint and parameters
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    params = {
        'lat': lat,
        'lon': lon
    }
    headers = {
        'User-Agent': 'MyWeatherApp/1.0 (jmrusso@bu.edu)'
    }

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")
        return

    forecast_time = data['properties']['meta']['updated_at']
    timeseries = data['properties']['timeseries']

    processed = [process_entry(entry,area,forecast_time) for entry in timeseries]

    return processed

#Read the csv file into a pandas dataframe
csv = pd.read_csv(CSV_PATH)

#Initialize a list to hold weather data
processed = []

#Process each row of the input csv
for _, row in csv.iterrows():
    area = row['Area']
    lat = row['Latitude']
    long = row['Longitude']
    area_data = process_area(area,lat,long)
    processed.extend(area_data)

#Filter out the invalid entries
filtered = filter(lambda x: x is not None, processed)

#Convert to pandas dataframe
df = pd.DataFrame(filtered)

#Write to csv
df.to_csv(OUTPUT_PATH,index = False)
