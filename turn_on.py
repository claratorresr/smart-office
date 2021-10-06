#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:42:36 2021

@author: manish
"""

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 16
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, True)
