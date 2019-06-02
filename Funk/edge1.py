#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(04,GPIO.IN,pull_up_down=GPIO.PUD_UP)


zeit=time.time()
t1=time.time()
delta_t=0
delta_t_alt=0
korrektur=0
korrektur_alt=0
while True:
  try: 
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
      schreiben=open("korrektur.txt","w")
      schreiben.write(str(korrektur_durch))
      schreiben.close()
  
# reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
GPIO.cleanup()


