#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import thread
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)

i=0
abstand=2.0
korrektur=0
while True:
  try: 
    #lesen=open("korrektur.txt","r")  
    #korrektur_str = lesen.read()      
    #lesen.close()
    #korrektur = float(korrektur_str)
    #print(korrektur)
    GPIO.wait_for_edge(23,GPIO.RISING)      
    t1 = time.time()
    GPIO.wait_for_edge(23,GPIO.FALLING)
    t2=time.time()
    zeit=t2-t1
    if(zeit < 0.002 and zeit > 0.001):
      print(korrektur)
      zeit=zeit+(0.002-zeit)*korrektur/100
    else:
      zeit=0.0015
    zeit=zeit-0.00006
    time.sleep(0.0164)
    GPIO.output(25, True)
    time.sleep(zeit)
    GPIO.output(25, False)
  
# reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
GPIO.cleanup()


