#!/usr/bin/python3

import core.config as conf
import core.weather as weather
import core.dashing as dashing
import core.web as web
import core.travel as travel
import core.database as db
import core.scamallpoll as cloud
import core.news as news
import core.datagather as data

import threading 
import time
from flask import Flask, render_template

app = Flask(__name__)

# Initalise the variables
temperature = 0
weatherForecast = ""
weatherIcon = ""
tubeStatus = "" 
bus93pty = "" 
bus93wim = ""
bus39pty = ""
bus39clp = "" 
coffeedata = ""
location =""
headlines=""

# Pull the data into the application 
def datagather():

  global temperature 
  global weatherForecast 
  global weatherIcon 
  global tubeStatus 
  global bus93pty 
  global bus93wim
  global bus39pty
  global bus39clp
  global coffeedata 
  global location 
  global headlines

  while True: 

    # Spawn weather... and wait?
    temperature = weather.weatherTemp() 
    temperature = (str(temperature) + "°C")
    
    weatherForecast = weather.weatherSummary()
    weatherIcon = weather.weatherIcon(weatherForecast)

    # Gather the tube data
    tubeStatus = travel.getTubeStatus()

    # Gather the bus data
    bus93pty = travel.getBusTime('490003146N')
    bus93wim = travel.getBusTime('490003146S')
    bus39pty = travel.getBusTime('490009097N')
    bus39clp = travel.getBusTime('490009097S')

    # Gather status information from openshift
    location = cloud.retrieveLocation()
    coffeedata = cloud.retrieveCoffeeStats()

    # Gather news
    headlines = news.retrieveHeadlines() 

# Data gathering function
datafetch = threading.Thread(name='datagather', target=datagather)
datagather.daemon = True
datafetch.start()

# Startup time to gather data on first load
time.sleep(5)

# Start our web applications
@app.route('/dashboard')
def dashboard():
  return render_template("nead.html", temp=temperature, forecast=weatherForecast, weathericon=weatherIcon, tubeStatus=tubeStatus, bus93pty=bus93pty, bus93wim=bus93wim, bus39pty=bus39pty, bus39clp=bus39clp,location=location,coffeedata=coffeedata,headlines=headlines)

@app.route('/wallpaper1')
def wallpaper():
  return render_template("wallpaper.html")

app.run(use_reloader=False,debug=True,port=5001)
