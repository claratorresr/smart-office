#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 11:47:39 2021

@author: manish
"""

import RPi.GPIO as GPIO
import time
from scd30_i2c import SCD30
from pushover import Client
import sys
# Initializing the SCD sensor
scd30 = SCD30()
# red led pin
red_led = 16
# client user_id and api_token for push notification
client = Client("usuus8pcfq8b2knfc5b12f6ikgiosu", api_token="aapd3ssp5fzri8h6kma6x99p2jocgo")

def main():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(red_led, GPIO.OUT)
    # set interval for data reading
    scd30.set_measurement_interval()
    scd30.start_periodic_measurement()
    
    time.sleep(2)
    
    while True:
        # setting up the sensor to get readings
        if scd30.get_data_ready():
            data = scd30.read_measurement()
            if data is not None:
                print(f"CO2: {data[0]:.2f}ppm, temp: {data[1]:.2f}'C, rh: {data[2]:.2f}%")
                # if co2 is greater than 2000 ppm or temperature is more than 26 degrees C
                if data[0]>2000 or data[1]>26:
                    GPIO.output(red_led, GPIO.HIGH)
                else:  
                    GPIO.output(red_led, GPIO.LOW)
                    #client.send_message("Open the window", title="CO2 Poisoning notification")
    
            time.sleep(2)
        else:
            time.sleep(0.2)
    
    
if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Quitting')
        GPIO.cleanup()
        sys.exit(0)
