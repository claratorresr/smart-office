import RPi.GPIO as GPIO
import time
"""
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
   print('Motion Detected!')

print('PIR Module Test (CTRL+C to exit)')
time.sleep(2)
print('Ready')

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(5)
except KeyboardInterrupt:
               print('Quit')
               GPIO.cleanup()
"""
import time
import RPi.GPIO as GPIO1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO1.setmode(GPIO1.BCM)
yellow_led=21
GPIO1.setup(yellow_led, GPIO1.OUT)
#GPIO.setup(PIR_PIN, GPIO.IN)


print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
    #print GPIO.input(PIR_PIN)
    #time.sleep(0.5)
    if GPIO.input(PIR_PIN):
        print('Motion Detected')
	GPIO1.output(yellow_led, GPIO1.HIGH)
        time.sleep(1)
    else:
        print('Motion Not Detected')
	GPIO1.output(yellow_led, GPIO1.LOW)
        time.sleep(1)
