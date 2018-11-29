#!/usr/bin/python3 
  
'''
Travel module
  
Gather the travel information for us
'''
  
import requests
import core.config as conf
import time
import datetime
  
def getTubeStatus():
  
    tflTubeURL = conf.configparse('tflLineStatusURL')
  
    tflTubeStatus = requests.get(tflTubeURL)
  
    jsonDump = tflTubeStatus.json()
  
    tubeStatus = jsonDump [0]['lineStatuses'][0]['statusSeverityDescription']
  
    return tubeStatus
  
  
def getBusTime(StopNumber):
  
    tflBusStatusURL = conf.configparse('tflBusStatusURL')
    tflAppID = conf.configparse('tflAppID')
    tflAppKey = conf.configparse('tflAppKey')
    timeCount = 0 
    busList = []
  
    tflBusURL = ( tflBusStatusURL + StopNumber + '/Arrivals?app_id=' + tflAppID + '&app_key=' + tflAppKey )
  
    tflBusData = requests.get(tflBusURL)
  
    jsonDump = tflBusData.json()
  
    for row in jsonDump:
  
        busTime = row['expectedArrival']
      
        # Cut to the characters we actually want
        busTime = busTime[11:16]

        busTimeObject = datetime.datetime.strptime(busTime, "%H:%M")

        # A dirty hack for BST
        busTime = busTimeObject + datetime.timedelta(hours=1)

        busTime = str(busTime)

        busTime = busTime[11:16]

        busList.append(busTime)

    # Sort the list of times
    busList.sort()

    joinedBus = ' '.join(busList)
    
    # Limit the count to three buses 
    busTimes = joinedBus[:17] 

    return busTimes
