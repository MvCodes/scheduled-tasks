import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat" : 12.99,
    "lon" : 77.75,
    "appid" : api_key,
    "cnt" : 4,

}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_ids = [weather_data["list"][i]["weather"][0]["id"] for i in range(parameters["cnt"])]
verdict = "Safe to go outside"
for weather_id in weather_ids:
    if int(weather_id) < 700:
        verdict = "Carry an umbrella"
        break


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='+19377447133',
  body=verdict,
  to='+917888876179'
)
print(message.status)


