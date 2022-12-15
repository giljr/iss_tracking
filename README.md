# iss_tracking
Python nternational Space Station (ISS) Tracking project in Python. Dez, 2022. Based on: Angela Yu 

## Can I track the ISS from my location?
Image result for this code will track the iss in the sky, comparing to your location and time.
The space station can be seen from over 6,700 locations worldwide. Enter your location to find out
when the space station will be flying overhead.
## Is the ISS visible every night?
It can only be seen when it is dawn or dusk at your location.
As such, it can range from one sighting opportunity a month to several a week,
since it has to be both dark where you are, and the space station has to happen to be going overhead.
## Resources:
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

## How-to run this app on [PyCharm 2022.3 (Community Edition)](https://www.jetbrains.com/pycharm/):

   0)  Open Pycharm, Clone this project by clicking Clone > VCS
       now, Git > Manage remotes... click + and paste:
       url: https://github.com/giljr/iss_tracking.git

   1) Run -> Edit Configurations -> Set Project Interpreter (lasted version - mine is Python 3.10)

   2) pip install requests (Terminal)

   3) pip install yagmail (Terminal)

   4) Go To Edit Configuration...Environment > Env. Variables
      and add two variable:
      EMAIL=<your_email>@gmail.com;
      EMAIL_PASS=<app_password>
      Sign in with App Passwords by following this tutorial:
      (https://support.google.com/accounts/answer/185833)

   5) run main (Shift+F10)

@editor: j3
Date: Dez, 2022
