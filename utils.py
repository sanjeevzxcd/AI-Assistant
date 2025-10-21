"""
Utility functions for AI Assistant
"""

import datetime
import requests
import wikipedia
import webbrowser
from config import WEATHER_API_KEY


def get_current_time():
    """Get the current time"""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


def get_current_date():
    """Get the current date"""
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y")


def search_wikipedia(query):
    """Search Wikipedia for information"""
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please be more specific. Options: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def search_web(query):
    """Open web browser with search query"""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Opening web search for: {query}"


def get_weather(city):
    """Get weather information for a city"""
    if not WEATHER_API_KEY:
        return "Weather API key not configured. Please add your OpenWeatherMap API key to config.py"
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {city} is {weather} with a temperature of {temp}°C"
        else:
            return f"Could not fetch weather data. {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"


def open_website(url):
    """Open a website in the default browser"""
    if not url.startswith('http'):
        url = 'https://' + url
    webbrowser.open(url)
    return f"Opening {url}"
