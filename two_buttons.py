# Customised C.L.A.S. script written by Michael Horne (@recantha)
# The board is placed on the GPIO so that the board overlaps the Pi.
# From the top (the end with the USB ports) to bottom, the following components were soldered:
# * Button 1
# * Red LED
# * Orange LED
# * Button 2
# When the button is pressed, the LED closest to it lights up, and when released the LED goes out.
# It should be possible for the buttons to work independently from one another so they can be on/off individually or together

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

button_1=5
red=11
button_2=22
orange=10

GPIO.setup(red,GPIO.OUT)
GPIO.setup(orange, GPIO.OUT)
GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(button_1) == False:
		GPIO.output(red,1)

	if GPIO.input(button_2) == False:
		GPIO.output(orange,1)

	if GPIO.input(button_1):
		GPIO.output(red,0)

	if GPIO.input(button_2):
		GPIO.output(orange,0)

	time.sleep(0.1)
