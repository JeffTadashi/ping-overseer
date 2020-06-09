# ping-overseer

This is a mass ping monitoring tool with the following features:

- Easily input a list of IP's from any source
- Ping monitors IP's in real time
- Constantly displays what IP's are down
- Highlights for longer downtime IP's

This is based on some functionality from PingInfoView. However, I needed something that ran on MacOS, thus this project was born!

I mainly use this for real-time work during network switch cutovers. It is meant to be a short-term tool (minutes/hours of usage), not something for monitoing over days.

## Installation

Get the latest version through PIP/PyPi:
```
sudo pip3 install --upgrade ping-overseer
```

NMAP application is also required, download that at: https://nmap.org

Then simply run as:
```
sudo ping-overseer -h
```

