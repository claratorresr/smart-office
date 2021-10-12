#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 11:47:39 2021

@author: manish
"""

# Initializing for motion sensor
import RPi.GPIO as GPIO
import time
# Initializing for led
import RPi.GPIO as GPIO1


GPIO.setmode(GPIO.BCM)
# Supress warnings
GPIO.setwarnings(False)
# Pin 4 for the sensor
PIR_PIN = 4
# pin 21 for yellow led
yellow_led=21



def main():
    
    # Setup the motion sensor
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Setup led
    GPIO1.setmode(GPIO1.BCM)
    
    GPIO1.setup(yellow_led, GPIO1.OUT)
    
    
    
    print('Starting up the PIR Motion sensor')
    time.sleep(1)                    
    print('Ready to take the readings')
                            
    while True:             
        #print GPIO.input(PIR_PIN)
        #time.sleep(0.5)
        if GPIO.input(PIR_PIN):
            print('Motion Detected')
            # If motion detected, switch on the led
            GPIO1.output(yellow_led, GPIO1.HIGH)
            time.sleep(2)
        else:
            print('Motion Not Detected')
            # If there's no motion, switch off the led
            GPIO1.output(yellow_led, GPIO1.LOW)
            time.sleep(2)
    
    
if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Quitting')
        GPIO.cleanup()
        pass








    
