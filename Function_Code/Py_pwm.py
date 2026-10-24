import RPi.GPIO as GPIO
import time
import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
	print("No controller found.")
	quit()

controller = pygame.joystick.Joystick(0)
controller.init()

print("Connected:", controller.get_name())

pin = 18
minpwm = 1
medpwm = 1.5
maxpwm = 2
freq = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, freq)
pwm.start(0)

def set_pwm(ms):
	duty = (ms * 5)
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	pwm.ChangeDutyCycle(0)
try:
	while True:
		pygame.event.pump()
		if controller.get_button(1) == 1:
			set_pwm(minpwm)
			print("servo set to right")
			time.sleep(0.5)
		elif controller.get_button(2) == 1:
			set_pwm(medpwm)
			print("servo set to middle")
			time.sleep(0.5)
		elif controller.get_button(3) == 1:
			set_pwm(maxpwm)
			print("servo set to left")
			time.sleep(0.5)
		time.sleep(0.1)

except KeyboardInterrupt:
	print("Stopping")

finally:
	pwm.stop()
	GPIO.cleanup
