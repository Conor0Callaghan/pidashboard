#!/bin/sh

nohup ./nead.py 2>&1 &

sleep 5

iceweasel http://localhost:5001/dashboard
