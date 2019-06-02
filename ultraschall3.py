#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    03.08.2013
# Last Update: 07.04.2015
#
# Copyright (c) 2013-2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

# import required modules
import time
import RPi.GPIO as GPIO

# define GPIO pins
GPIOTrigger = 23
GPIOEcho    = 22

# function to measure the distance
def MeasureDistance():
  # set trigger to high
  GPIO.output(GPIOTrigger, True)

  # set trigger after 10µs to low
  time.sleep(0.00001)
  GPIO.output(GPIOTrigger, False)

  # store initial start time
  StartTime = time.time()

  # store start time
  while GPIO.input(GPIOEcho) == 0:
    StartTime = time.time()

  # store stop time
  while GPIO.input(GPIOEcho) == 1:
    StopTime = time.time()

  # calculate distance
  TimeElapsed = StopTime - StartTime
  Distance = (TimeElapsed * 34300) / 2

  return Distance

# main function
def main():
  try:
    speed=[0.0]*30
    i=0
    Distance = MeasureDistance()
    Distance_old = Distance
    Distance_print_old= Distance
    data = []
    timel = []
    while True:
      if i >=30:
        i=0
      Distance = MeasureDistance()
      if Distance < 400:
        Distance_old_old = Distance_old
        Distance_old=Distance
        Distance_print = (Distance + Distance_old_old + Distance_old) /3 
        speed[i] = (Distance_print_old - Distance_print)*10
        print(speed[i])
        Distance_print_old=Distance_print
        print("Measured Distance median = %.1f cm" % Distance_print)
        speed_median =sum(speed)/float(len(speed))
        print("Measured speed median = %.1f cm/s" %  speed_median )
        i=i+1
	
	#data.append(Distance_print)
	#timel.append(time.time())
	
      #else:
        #print(">50 Aussortiert")
      #print("Measured Distance = %.1f cm" % Distance)
      time.sleep(0.02)
      

  # reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    
    #np.savetxt("ultra.txt", np.column_stack((timel,data)))
    GPIO.cleanup()

if __name__ == '__main__':
  # use GPIO pin numbering convention
  GPIO.setmode(GPIO.BCM)

  # set up GPIO pins
  GPIO.setup(GPIOTrigger, GPIO.OUT)
  GPIO.setup(GPIOEcho, GPIO.IN)

  # set trigger to false
  GPIO.output(GPIOTrigger, False)

  # call main function
  main()