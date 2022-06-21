#!/usr/bin/env python3
from __future__ import print_function
import RPi.GPIO as GPIO
import time
import sys
import requests
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
zone1 = 7 #Large Lawn, closer to garage
zone2 = 13 #Lawn by Street & Tree
zone3 = 15 #Large Lawn, Next to sidewalk
zone4 = 16 #Small Lawn with Roses
GPIO.setup(zone1, GPIO.OUT)
GPIO.setup(zone2, GPIO.OUT)
GPIO.setup(zone3, GPIO.OUT)
GPIO.setup(zone4, GPIO.OUT)

def main():
      url = "https://api.openweathermap.org/data/2.5/weather?lat=37.266419&lon=-121.937272&appid=5f048eb90857f17e9daa1f1df6d5c701"
      response = requests.request("GET",url)
      print('')
      print('')
      print('OpenWeather Map Response:')
      x = response.text
      y = json.loads(x)
      curweath = y["weather"]
      for item in curweath:
              results = item
              print(results["main"])
              if results["main"] == "Clear":
                      print("It's Clear Sailing today! \n Begin Watering")
              elif results["main"] == "Rain":
                      print("We don't water the grass when it's raining\n Ignoring request")
                      exit()
              else:
                      print("IDK, look outside?")
      GPIO.output(zone1, GPIO.HIGH)
      GPIO.output(zone2, GPIO.HIGH)
      GPIO.output(zone3, GPIO.HIGH)
      GPIO.output(zone4, GPIO.HIGH)
      #GPIO.output(zone1, GPIO.LOW)
      #time.sleep(300)
      #GPIO.output(zone1, GPIO.HIGH)
      #time.sleep(5)
      #GPIO.output(zone2, GPIO.LOW)
      #time.sleep(900)
      #GPIO.output(zone2, GPIO.HIGH)
      #time.sleep(5)
      #GPIO.output(zone3, GPIO.LOW)
      #time.sleep(450)
      #GPIO.output(zone3, GPIO.HIGH)
      #time.sleep(5)
      GPIO.output(zone4, GPIO.LOW)
      time.sleep(960)
      GPIO.output(zone4, GPIO.HIGH)
      exit()
      
if __name__ == "__main__":
