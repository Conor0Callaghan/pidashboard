#!/usr/bin/python3

import requests
import json 
import pprint
import re

"""
Function comments
"""

def weatherTemp():

    # HACKERY
    weatherUrl= 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/'
    weatherFormat='json'
    weatherLocation= '3772'
    weatherApiKey='XXXXX'
 
    # Generate the full URL we need to poll with variables
    weatherFullUrl = (weatherUrl + weatherFormat + '/' +  weatherLocation + "?res=hourly&key=" + weatherApiKey)

    data = requests.get(weatherFullUrl)

    jsonDump = data.json()

    # Parse the JSON tree to grab the values we want
    currentTemp = jsonDump ['SiteRep']['DV']['Location']['Period'][1]['Rep'][-1]['T']

    return currentTemp 

"""
Function comments
"""

def weatherSummary():

    regionalURL = 'http://datapoint.metoffice.gov.uk/public/data/txt/wxfcs/regionalforecast/json/514?key=XXXXXX'
    regionalData = requests.get(regionalURL)

    jsonDump = regionalData.json()

    regionalSummary = jsonDump ['RegionalFcst']['FcstPeriods']['Period'][0]['Paragraph'][0]['$']

    return regionalSummary

"""
A simple function to decide on which icon to display in the weather panel of 
the dashboard

Inputs: weatherForecast 
"""

def weatherIcon(weatherForecast):

    """
    I wish python had case statements

    Search the forecast for some strings and return the icon based on the 
    content
    """

    if re.search(r'(?i)rain', weatherForecast):
        weatherIcon = "wi-rain"
    elif re.search(r'(?i)wind', weatherForecast) and re.search(r'(?i)rain', weatherForecast):
        weatherIcon = "wi-rain-wind"
    elif re.search(r'(?i)sun', weatherForecast) or re.search(r'(?i)sunny', weatherForecast):
        weatherIcon = "wi-day-sunny"
    elif re.search(r'(?i)cloud\D', weatherForecast):
        weatherIcon = "wi-day-cloudy"
    elif re.search(r'(?i)thunder', weatherForecast):
        weatherIcon = "wi-lightning"
    elif re.search(r'(?i)shower[s]', weatherForecast):
        weatherIcon = "wi-day-showers"
    else: 
        weatherIcon = "???"

    weatherIcon = ("wi " + weatherIcon)

    return weatherIcon
