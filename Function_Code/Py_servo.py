import RPi.GPIO as GPIO
import time

pin = 18
minpwm = 1
medpwm = 1.5
maxpwm = 2
freq = 50 #20 ms

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, freq)
pwm.start(0)

def set_pwm(this):
	duty = (this * 5)
	pwm.ChangeDutyCycle(duty)

try:
	while True:
#If Joystick does button:
		set_pwm(minpwm)
		print("servo set to right")
		time.wait(1)
#ElseIf Joystick does button:
		set_pwm(medpwm)
		print("setvo set to middle")
		time.wait(1)
#ElseIf Joystick does button:
		set_pwm(maxpwm)
		print("servo set to left")
		time.wait(1)

		time.wait(0.1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup