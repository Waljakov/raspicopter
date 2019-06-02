#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(04,GPIO.IN,pull_up_down=GPIO.PUD_UP)

ulti1_a=3.5476

class ulti1(threading.Thread):
  def run(self):
    while True:
      try: 
        GPIO.wait_for_edge(04,GPIO.RISING)      
        t1 = time.time()
        GPIO.wait_for_edge(04,GPIO.FALLING)
        t2=time.time()
        t_ulti1=t2-t1
        if((t_ulti1)*170)<4:
          print("Zeit in s ulti:")
          print(t_ulti1)
          print("Abstand in m:")
          ulti1_a=(t_ulti1)*170
          print(ulti1_a)
    # reset GPIO settings if user pressed Ctrl+C
      except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
      

class funk1(threading.Thread):
  def run(self):
    while True:
      try: 
        GPIO.wait_for_edge(23,GPIO.RISING)      
        t1 = time.time()
        GPIO.wait_for_edge(23,GPIO.FALLING)
        t2=time.time()
        print("Zeit in s funk:")
        print(t2-t1)
        print(ulti1_a)
        if 0.0008 < (t2-t1) < 0.002:
          GPIO.output(25, True)
          time.sleep(t2-t1)
          GPIO.output(25, False)
    # reset GPIO settings if user pressed Ctrl+C
      except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()


  
ulti1().start()
funk1().start()
GPIO.cleanup()

 

