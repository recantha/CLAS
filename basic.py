# Basic script for C.L.A.S. written by Andrew Gale (@AndrewGale3)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button = 22
red = 5
yellow = 11
green = 10

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button_and_pause():
	if GPIO.input(button):
		time.sleep(1)
	else:
		time.sleep(0.1)

for i in range(3):
	GPIO.output(red,1)
	check_button_and_pause()
	GPIO.output(red,0)

	GPIO.output(yellow,1)
	check_button_and_pause()
	GPIO.output(yellow,0)

	GPIO.output(green,1)
	check_button_and_pause()
	GPIO.output(green,0)

GPIO.cleanup()
