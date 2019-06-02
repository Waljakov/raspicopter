#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
  try: 
    GPIO.wait_for_edge(24,GPIO.RISING)      
    t1 = time.time()
    GPIO.wait_for_edge(24,GPIO.FALLING)
    t2=time.time()
    if((t2-t1)*170)< 4:
      print("Zeit in s:")
      print(t2-t1)
      print("Abstand in m:")
      print((t2-t1)*170)
  
# reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
GPIO.cleanup()


