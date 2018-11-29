#!/usr/bin/python3

import core.config as conf
import core.weather as weather
import core.dashing as dashing
import core.web as web
import core.travel as travel
import core.database as db
import core.scamallpoll as cloud

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

  while True: 

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

    time.sleep(60):