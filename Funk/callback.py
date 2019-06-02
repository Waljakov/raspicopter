#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(04,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)




def my_callback(channel):
  global t1
  #print("1\n")
  if GPIO.input(04):
    t1 = time.time()
  else:
    global delta_t
    global delta_t_alt
    global korrektur
    global korrektur_alt
    global zeit
    #print(t1) 
    #GPIO.wait_for_edge(04,GPIO.RISING) 
    #print(t1-t1_alt)  
    #GPIO.wait_for_edge(04,GPIO.FALLING)
    t2=time.time()
    #print(t2)
    zeit_alt= zeit
    delta_t_alt2=delta_t_alt
    delta_t_alt=delta_t
    zeit=t2-t1
    delta_t=zeit_alt-zeit
    v_durch=(delta_t_alt2*170*4+delta_t_alt*170*4+delta_t*170*4)/3
    korrektur_alt2=korrektur_alt
    korrektur_alt=korrektur
    if(v_durch != 0):
      if((zeit*170/v_durch)<10 and v_durch>0):
        korrektur=100-zeit*170*10/v_durch
      else:
        korrektur=0
    else:
     korrektur=0
    korrektur_durch=(korrektur+korrektur_alt+korrektur_alt2)/3
    t1_alt=t1 
    #if((t2-t1)*170)<4:
      #print("Zeit in s:")
      #print(t2-t1)
      #print("Abstand in m:")
      #print((t2-t1)*170)
      #print("Geschwindigkeit")
      #print(delta_t*170*4)
      #print(delta_t_alt*170*4)
      #print(delta_t_alt2*170*4)
      #print(v_durch)
    #print(korrektur)
      #print(korrektur_alt)
      #print(korrektur_alt2)
      #print(korrektur_durch)
      #print("--------------")
      #schreiben=open("korrektur.txt","w")
      #schreiben.write(str(korrektur_durch))
      #schreiben.close()

def my_callback2(channel):
  global t1_2
  global korrektur
  global status
  
  if GPIO.input(23):     
    t1_2 = time.time()
    GPIO.output(25, True)
    #print("2.1\n")
  else:
    #print("2.2\n")
    t2=time.time()
    zeit_2=t2-t1_2
    if(zeit_2 < 0.002 and zeit_2 > 0.001):
      #print(korrektur)
      zeit_2=zeit_2+(0.002-zeit_2)*korrektur/100
    else:
      zeit_2=0.0015
    zeit_2=zeit_2-0.00006
    #time.sleep(0.0166)
    #print(zeit_2)
    #print((0.002-zeit_2))
    if (status==1):
      time.sleep((0.002-zeit_2)*korrektur/100)
    GPIO.output(25, False)


def channel6(channel):
  global start
  global status
  if GPIO.input(20):
    start=time.time()
  else:
    start2=time.time()
    diff=start2-start
    #print(diff)
    if(diff>0.0015 and diff<0.004):
      status = 1
    else:
      status = 0


    
  

global status
status = 0
global start
start = time.time()
global t1
t1=time.time()
global delta_t
global delta_t_alt
global korrektur
global korrektur_alt
global zeit
delta_t=0
global t1_2
t1_2=time.time()
delta_t_alt=0
korrektur=0
korrektur_alt=0
zeit=time.time()
GPIO.add_event_detect(04,GPIO.BOTH, callback=my_callback)
GPIO.add_event_detect(23,GPIO.BOTH, callback=my_callback2)
GPIO.add_event_detect(20,GPIO.BOTH, callback=channel6)

while 1:
  try:
    GPIO.output(27, True)
    time.sleep(0.001)
    GPIO.output(27, False)
    time.sleep(0.1)
# reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
    sys.exit()
GPIO.cleanup()





  













