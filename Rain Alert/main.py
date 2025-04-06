import requests
from twilio.rest import Client
# To get the weather data, I have used openweather API
# To send text SMS I have used Twillo API

api_key = "252e8f33973cbe29b689b6f14f0bfd2b"

account_sid = "[Account SID number]"
auth_token = "[Secret key]"

parameters = {"lat": 18.484240, "lon": 73.805473, "cnt": 4, "appid": api_key}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring an umbrella with you today. It will Rain!!",
            from_='[TWILIO Number]',
            to='[YOUR NUMBER]'
        )
    print(message.status)

# To run the program every 3 hours use python anywhere so that u don't need to run everytime you go out

