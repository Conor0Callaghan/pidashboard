#!/usr/bin/python3

""" Functions to pull data from hosted python """

import requests
import core.config as config

def retrieveLocation():

    locationURL = ( 'http://' + config.configparse('openshiftDomain') + '/' + config.configparse('openshiftLocationPath' ) + '/display' )

    locationDetailData = requests.get(locationURL)
  
    locationDetail = locationDetailData.text

    # Do the logic on the location, make this into a list?  
    if ( locationDetail == "location1" ):
       location = "In the office"
    elif ( locationDetail == "location2" ):
       location = "Travelling"
    elif ( locationDetail == "location3" ):
       location = "Coffee break"
  
    return location

def retrieveCoffeeStats():

    coffeeStatus = ""

    coffeeURL = ( 'http://' + config.configparse('openshiftDomain') + '/' + config.configparse('openshiftCoffeeStatus') )

    coffeeData = requests.get(coffeeURL)

    coffeeDataDetail = coffeeData.text

    coffeeDataDetail = int(coffeeDataDetail)

    for count in range(0,coffeeDataDetail):
      coffeeStatus = coffeeStatus + "☕"

    return coffeeStatus
