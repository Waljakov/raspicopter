#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import thread
import RPi.GPIO as GPIO





korrektur_durch=0

def modify(threadname,korrektur_durch):

  print("start 1")
  while True:
    time.sleep(0.01)
    GPIO.wait_for_edge(23,GPIO.RISING)      
    time1 = time.time()
    GPIO.wait_for_edge(23,GPIO.FALLING)
    time2=time.time()
    zeit_m=time2-time1
    if(zeit_m < 0.002 and zeit_m > 0.001):
      print(korrektur_durch)
      zeit_m=zeit_m+(0.002-zeit_m)*korrektur_durch/100
    else:
      zeit_m=0.0015
    zeit_m=zeit_m-0.00006
    time.sleep(0.0164)
    GPIO.output(25, True)
    time.sleep(zeit_m)
    GPIO.output(25, False)

def korrekt(threadname, korrektur_durch):

  zeit=time.time()
  t1=time.time()
  delta_t=0
  korrektur=0
  delta_t_alt=0
  korrektur_alt=0
  print("start 2")
  while True:
    GPIO.wait_for_edge(04,GPIO.RISING) 
    t1_alt=t1 
    t1 = time.time()
    #print(t1-t1_alt)  
    GPIO.wait_for_edge(04,GPIO.FALLING)
    t2=time.time()
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
    if((t2-t1)*170)<4:
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
      print(korrektur_durch)
      print("--------------")
      #schreiben=open("korrektur.txt","w")
      #schreiben.write(str(korrektur_durch))
      #schreiben.close()

try: 
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
  GPIO.setup(25, GPIO.OUT)
  GPIO.setup(04,GPIO.IN,pull_up_down=GPIO.PUD_UP)
  thread.start_new_thread(modify,("Run Modify",korrektur_durch,))
  thread.start_new_thread(korrekt,("Run Korrekt",korrektur_durch,))
  print("durch")
except KeyboardInterrupt:
  print("Measurement stopped by user")
  GPIO.cleanup()
except:
  print("error")


while 1:
 pass
GPIO.cleanup() 

