### --- IMPORTS --- ### 

#we want requests to get our api data
import requests
#we want dot env and os for env variables
from dotenv import load_dotenv
import os
#finally we want twilio for the sms function
from twilio.rest import Client

### --- ENV VARIABLES --- ### 

#we want to load our env
load_dotenv()

#we use load_dotenv and os to grab our variables now
lat = float(os.getenv("LATITUDE"))
lon = float(os.getenv("LONGITUDE"))
api = str(os.getenv("API_KEY"))

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
sending = os.getenv('SENDING_NUMBER')
receiving = os.getenv('RECEIVING_NUMBER')

### --- REQUESTS --- ###

#we are making a call to this
api_call_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
#we now need params for the call
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api,
}
#we now want to get our api request
response = requests.get(api_call_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#we now want to get the weather over 12 hours for this we can loop through the json data to do this we get a slice of the data
#gets the first 12 entries of weather data in the hourly category
weather_slice = weather_data["hourly"][:12]

#now we loop through it to get the codes for each piece
for hourly_data in weather_slice:
    #we now get the data
    global WILL_RAIN
    codes = hourly_data["weather"][0]["id"]
    #now we want ones under 700 for rain alerts
    if codes < 700:
        WILL_RAIN = True
        break

print(WILL_RAIN)
        
### --- SEND ALERT --- ###

#now we have the weather alert that it WILL rain in the next 12 hours we can tell the user to bring an umbrella
if WILL_RAIN:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Hey! This is your rain alert message! It's gonna rain in the next 12 hours D: Please bring an umbrella!.",
                        from_=sending,
                        to=receiving
                    )
    
    print(message.sid)