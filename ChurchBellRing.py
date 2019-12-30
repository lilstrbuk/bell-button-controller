import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False) # ignore
RELAIS_1_GPIO = 17 # GPIO to command relay
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Using GPIO pin numbers, Pin 15 is set as input and default off

def turnOn():
	GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

def turnOff():
	GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

if not (len(sys.argv) - 1): # missing on/off var and run time
	print("Call some vars")

elif sys.argv[1] == "off":
	turnOff()

elif not (len(sys.argv) - 2): # prevents it from being turned on forever
	print("do that again")

elif sys.argv[1] == "on" and not float(sys.argv[2]) == 0: # sys.argv is the command the [bracketed number is which arguemnt 1:on/off 2:seconds]
	turnOn() 
	time.sleep(float(sys.argv[2])) #is on but waits
	turnOff()

elif GPIO.input(15) == GPIO.HIGH: # tests button position  NEED way to make sure it does not get stuck here
		turnOn()
		print("button being pressed")

else:
	#turnOff()
	print("pass")
