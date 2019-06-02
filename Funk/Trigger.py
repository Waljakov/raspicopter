#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import RPi.GPIO as GPIO

# define GPIO pins
GPIOTrigger = 27



# main function
def main():
  try:
    while True:
    # set trigger to high
      GPIO.output(GPIOTrigger, True)
      time.sleep(0.001)
      GPIO.output(GPIOTrigger, False)
      time.sleep(0.1)
  # reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
  

if __name__ == '__main__':
  # use GPIO pin numbering convention
  GPIO.setmode(GPIO.BCM)

  # set up GPIO pins
  GPIO.setup(GPIOTrigger, GPIO.OUT)
  #GPIO.setup(GPIOEcho, GPIO.IN)

  # set trigger to false
  GPIO.output(GPIOTrigger, False)

  # call main function
  main()
