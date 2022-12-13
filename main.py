'''
International Space Station (ISS) Tracking Project

Can I track the ISS from my location?
Image result for this code will track the iss in the sky, comparing to your location and time.
The space station can be seen from over 6,700 locations worldwide. Enter your location to find out
when the space station will be flying overhead.

Is the ISS visible every night?
It can only be seen when it is dawn or dusk at your location.
As such, it can range from one sighting opportunity a month to several a week,
since it has to be both dark where you are, and the space station has to happen to be going overhead.
Resources:

JSON Viewer - Chrome Web Store:
https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh

Latitude and Longitude Finder:
https://www.latlong.net/

Sunset and sunrise times API:
https://sunrise-sunset.org/api

International Space Station Current Location:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
Location: Porto Velho Ro - Brazil


Inspired in Angela Yu's ISS Project:
https://www.udemy.com/course/100-days-of-code/

@editor: j3
Date: Dez, 2022
'''

from datetime import datetime, timedelta
import requests
import yagmail
import os

global is_iss_overhead
is_iss_overhead = False
global is_night
is_night = False

MY_LAT = -8.761070
MY_LNG = -63.885980

timezone_hour_offset = -4
input_format = "%Y-%m-%dT%H:%M:%S+00:00"  # works for this site because UTC is guaranteed.
output_format = "%H:%M:%S"

EMAIL = os.environ['EMAIL']
EMAIL_PASS = os.environ['EMAIL_PASS']

'''
The ISS is visible only at night :/
'''
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "date": "today",
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_date_time = data["results"]["sunrise"]
    sunset_date_time = data["results"]["sunset"]

    sunrise = datetime.strptime(sunrise_date_time, input_format)
    local_sunrise = sunrise + timedelta(hours=timezone_hour_offset)

    sunset = datetime.strptime(sunset_date_time, input_format)
    local_sunset = sunset + timedelta(hours=timezone_hour_offset)
    local_sunrise_hour = local_sunrise.hour
    local_sunset_hour = local_sunset.hour
    time_now = datetime.now().hour
    print(f"Local time: {time_now} hours")
    if time_now >= local_sunset_hour or time_now <= local_sunrise_hour:
        is_night = True

'''
Spot the Station" find out if the International Space Station, 
the third brightest object in the sky, is going to pass above your location.
Your position is within + or - 5 degrees of the ISS position.
'''
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    print(f"iss_lat:{iss_lat}, iss_lng:{iss_lng}")
    print(f"my__lat:{MY_LAT},my__lng:{MY_LNG}")
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= iss_lng + 5:
        is_iss_overhead = True

'''
Sends alerts via your email using yagmail.
Please set environment variables in PyCharm, follow stackoverflow:
https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm
'''
def send_email():
    user = yagmail.SMTP(user=EMAIL, password=EMAIL_PASS)
    user.send(to=EMAIL, subject="Look Up 👆️", contents="The ISS is above you in the sky.")

is_night()
is_iss_overhead()

is_night

if is_night == True:
    print("Is night :)")
else:
    print("Is not night :/\n")

if is_iss_overhead == True:
    print("ISS is overhead :)")
else:
    print("ISS is not overhead :/ ")

if is_iss_overhead is True and is_night is True:
    send_email()