import requests
from pprint import pprint
API_Key="533956744e7c028c86b0253c2beece7e"
location = input("Enter Your Desired Location: ")
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_Key}"
#final_url = weather_url + API_Key
weather_data = requests.get(weather_url).json()
pprint(weather_data)