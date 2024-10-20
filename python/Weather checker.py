import requests
from datetime import datetime, timedelta

# Function to get weather data from OpenWeatherMap API
def get_weather(city_name, api_key):
    # API endpoint for 7-day weather forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}"
    
    # Send the request to OpenWeatherMap API
    response = requests.get(url)
    
    # If the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please check the city name or API key.")
        return None

# Function to display weekly weather forecast
def display_weekly_weather(weather_data):
    if weather_data:
        print(f"Weather forecast for {weather_data['city']['name']}, {weather_data['city']['country']}:")

        # The forecast comes in 3-hour intervals, so we will filter one forecast per day
        current_date = None
        for forecast in weather_data['list']:
            forecast_time = datetime.utcfromtimestamp(forecast['dt'])
            forecast_date = forecast_time.date()
            
            # Check if it's a new day
            if current_date != forecast_date:
                current_date = forecast_date
                
                # Get relevant weather information
                temp = forecast['main']['temp']
                weather_description = forecast['weather'][0]['description']
                wind_speed = forecast['wind']['speed']
                
                # Display weather for the day
                print(f"\nDate: {forecast_date}")
                print(f"  Temperature: {temp}°C")
                print(f"  Weather: {weather_description}")
                print(f"  Wind Speed: {wind_speed} m/s")
                
    else:
        print("No weather data available.")

# Main program
if __name__ == "__main__":
    # Your OpenWeatherMap API key (replace with your own key)
    api_key = "your_openweathermap_api_key"
    
    # Ask user for the city they want the forecast for
    city_name = input("Enter the city name for weather forecast: ")
    
    # Get weather data
    weather_data = get_weather(city_name, api_key)
    
    # Display the weekly weather forecast
    display_weekly_weather(weather_data)
