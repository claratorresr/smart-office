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
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')

while True:
  if GPIO.input(PIR_PIN):
    print('Motion Detected')
    time.sleep(1)
  else:
    print('Motion Not Detected')
    time.sleep(1)
