import time
import dht11
import RPi.GPIO as GPIO

#define GPIO 14 as DHT11 data pin
Temp_sensor=14
red_led = 18
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  # Initialise display
#  lcd_init()
  GPIO.setup(red_led, GPIO.OUT)
  instance = dht11.DHT11(pin = Temp_sensor)

  while True:
        #get DHT11 sensor value
        result = instance.read()
        if result.temperature >= 20:
	  GPIO.output(red_led, GPIO.HIGH)
          time.sleep(1)
	else:
	  print"temperature is low"

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)
