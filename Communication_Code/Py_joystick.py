import pygame

pygame.init()
pygame.joystick.init()

if  pygame.joystick.get_count() == 0:
	print("No controller found.")
	quit()

controller = pygame.joystick.Joystick(0)
controller.init()

print("Connected:", controller.get_name())

while True:
	pygame.event.pump()

	left_x = controller.get_axis(0)
	left_y = controller.get_axis(1)

	a_button = controller.get_button(0)
	b_button = controller.get_button(1)

	print("LX: ", left_x, "LY: ", left_y, "A: ", a_button, "B: ", b_button)
