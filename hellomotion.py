import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pir = 21
GPIO.setup(pir,GPIO.IN)
time.sleep(2)
while True:
	if GPIO.input(pir):
		print("motion dected")
		time.sleep(0.5)
	else:
		print("nothing")
		time.sleep(0.5)
GPIO.cleanup()
