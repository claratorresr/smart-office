import RPi.GPIO as GPIO
import time
from scd30_i2c import SCD30
from pushover import Client
# Initializing the SCD sensor
scd30 = SCD30()
# client user_id and api_token for push notification
client = Client("usuus8pcfq8b2knfc5b12f6ikgiosu", api_token="aapd3ssp5fzri8h6kma6x99p2jocgo")
GPIO.setmode(GPIO.BCM)
red_led = 16
GPIO.setup(red_led, GPIO.OUT)
scd30.set_measurement_interval(2)
scd30.start_periodic_measurement()

time.sleep(2)

while True:
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        if m is not None:
            print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
            if m[0]>2000 or m[1]>26:
                GPIO.output(red_led, GPIO.HIGH)
                time.sleep(2)
                GPIO.output(red_led, GPIO.LOW)
                #client.send_message("Open the window", title="CO2 Poisoning notification")

        time.sleep(2)
    else:
        time.sleep(0.2)

# Code for push notification
"""
from pushover import Client
client = Client("usuus8pcfq8b2knfc5b12f6ikgiosu", api_token="aapd3ssp5fzri8h6kma6x99p2jocgo")
client.send_message("Open the window", title="CO2 Poisoning notification")
"""
